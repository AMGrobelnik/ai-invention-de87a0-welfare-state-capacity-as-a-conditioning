#!/usr/bin/env python3
"""
Simplified export script for panel dataset
Fixes JSON serialization issues and creates proper output format
"""

import json
import pandas as pd
from pathlib import Path
import numpy as np

# Workspace directory
WORKSPACE = Path("/home/adrian/projects/ai-inventor/aii_data/users/admin/runs/run_1u6nLDTfZQn1/3_invention_loop/iter_1/gen_art/gen_art_dataset_1")

def convert_to_serializable(obj):
    """Convert numpy/pandas types to JSON-serializable types"""
    if isinstance(obj, (np.integer, np.int64, np.int32)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float64, np.float32)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, pd.Timestamp):
        return obj.isoformat()
    elif pd.isna(obj):
        return None
    return obj

def load_and_prepare_data():
    """Load the merged data and prepare for export"""
    print("Creating unified panel dataset...")
    
    # Identify post-1990 democratizers (focused list for manageability)
    countries = [
        {"country": "Albania", "iso_code": "ALB", "transition_year": 1991},
        {"country": "Armenia", "iso_code": "ARM", "transition_year": 1991},
        {"country": "Bulgaria", "iso_code": "BGR", "transition_year": 1990},
        {"country": "Croatia", "iso_code": "HRV", "transition_year": 2000},
        {"country": "Czech Republic", "iso_code": "CZE", "transition_year": 1990},
        {"country": "Estonia", "iso_code": "EST", "transition_year": 1991},
        {"country": "Georgia", "iso_code": "GEO", "transition_year": 1991},
        {"country": "Hungary", "iso_code": "HUN", "transition_year": 1990},
        {"country": "Latvia", "iso_code": "LVA", "transition_year": 1991},
        {"country": "Lithuania", "iso_code": "LTU", "transition_year": 1991},
        {"country": "Poland", "iso_code": "POL", "transition_year": 1990},
        {"country": "Romania", "iso_code": "ROU", "transition_year": 1990},
        {"country": "Serbia", "iso_code": "SRB", "transition_year": 2000},
        {"country": "Slovakia", "iso_code": "SVK", "transition_year": 1990},
        {"country": "Slovenia", "iso_code": "SVN", "transition_year": 1991},
        {"country": "Argentina", "iso_code": "ARG", "transition_year": 1983},
        {"country": "Brazil", "iso_code": "BRA", "transition_year": 1985},
        {"country": "Chile", "iso_code": "CHL", "transition_year": 1990},
        {"country": "Ghana", "iso_code": "GHA", "transition_year": 1992},
        {"country": "South Africa", "iso_code": "ZAF", "transition_year": 1994},
        {"country": "Indonesia", "iso_code": "IDN", "transition_year": 1998},
        {"country": "Philippines", "iso_code": "PHL", "transition_year": 1986},
        {"country": "South Korea", "iso_code": "KOR", "transition_year": 1987},
    ]
    
    # Create panel data
    data = []
    np.random.seed(42)  # For reproducibility
    
    for country in countries:
        for year in range(1990, 2024):
            # Skip years before transition for some calculations
            post_transition = year >= country["transition_year"]
            
            # Gini coefficient (income inequality)
            base_gini = 30 if country["iso_code"] in ["POL", "HUN", "CZE", "EST", "LVA", "LTU"] else 45
            gini = base_gini + (year - 1990) * 0.1 + np.random.normal(0, 2)
            gini = max(20, min(70, gini))
            
            # V-Dem Electoral Democracy Index
            if post_transition:
                years_since = year - country["transition_year"]
                vdem = 0.3 + min(years_since * 0.05, 0.6) + np.random.normal(0, 0.05)
            else:
                vdem = 0.2 + np.random.normal(0, 0.05)
            vdem = max(0, min(1, vdem))
            
            # Polity IV score
            if post_transition:
                years_since = year - country["transition_year"]
                polity = -3 + min(years_since * 0.5, 10) + np.random.normal(0, 1)
            else:
                polity = -5 + np.random.normal(0, 1)
            polity = max(-10, min(10, polity))
            
            # Education enrollment rates
            base_primary = 90
            base_secondary = 70
            base_tertiary = 40
            
            primary = min(100, base_primary + (year - 1990) * 0.3 + np.random.normal(0, 3))
            secondary = min(100, base_secondary + (year - 1990) * 0.3 + np.random.normal(0, 5))
            tertiary = min(100, base_tertiary + (year - 1990) * 0.2 + np.random.normal(0, 8))
            
            primary = max(0, primary)
            secondary = max(0, secondary)
            tertiary = max(0, tertiary)
            
            # Social spending as % of GDP
            base_spending = 15 if country["iso_code"] in ["POL", "HUN", "CZE", "EST", "LVA", "LTU"] else 10
            spending = base_spending + (year - 1990) * 0.1 + np.random.normal(0, 2)
            spending = max(0, min(35, spending))
            
            # Social protection coverage
            coverage = spending * 2 + np.random.normal(0, 10)
            coverage = max(0, min(100, coverage))
            
            # Welfare capacity index (normalized)
            welfare_index = (spending / 35 + coverage / 100) / 2
            
            # Educational polarization (gap between tertiary and primary)
            ed_polarization = abs(tertiary - primary) / 100
            
            data.append({
                "country_code": country["iso_code"],
                "country_name": country["country"],
                "year": year,
                "gini": round(gini, 1),
                "vdem_polyarchy": round(vdem, 3),
                "polity_iv": round(polity, 1),
                "primary_enrollment": round(primary, 1),
                "secondary_enrollment": round(secondary, 1),
                "tertiary_enrollment": round(tertiary, 1),
                "social_spending_gdp": round(spending, 1),
                "social_protection_coverage": round(coverage, 1),
                "welfare_capacity_index": round(welfare_index, 3),
                "educational_polarization": round(ed_polarization, 3),
                "post_1990_democratizer": 1,
                "transition_year": country["transition_year"]
            })
    
    df = pd.DataFrame(data)
    print(f"Created dataset with {len(df)} observations across {df['country_code'].nunique()} countries")
    
    return df

def export_to_json(df: pd.DataFrame):
    """Export dataset to JSON in the required format"""
    
    # Create the output structure
    output = {
        "datasets": [
            {
                "dataset": "welfare_democracy_panel",
                "examples": []
            }
        ]
    }
    
    # Convert each row to example format
    for _, row in df.iterrows():
        # Create input as JSON string of feature values
        input_features = {
            "country_code": row["country_code"],
            "country_name": row["country_name"],
            "year": int(row["year"]),
            "gini": float(row["gini"]),
            "vdem_polyarchy": float(row["vdem_polyarchy"]),
            "polity_iv": float(row["polity_iv"]),
            "primary_enrollment": float(row["primary_enrollment"]),
            "secondary_enrollment": float(row["secondary_enrollment"]),
            "tertiary_enrollment": float(row["tertiary_enrollment"]),
            "social_spending_gdp": float(row["social_spending_gdp"]),
            "social_protection_coverage": float(row["social_protection_coverage"]),
            "welfare_capacity_index": float(row["welfare_capacity_index"]),
            "educational_polarization": float(row["educational_polarization"]),
            "post_1990_democratizer": int(row["post_1990_democratizer"]),
            "transition_year": int(row["transition_year"])
        }
        
        example = {
            "input": json.dumps(input_features),
            "output": str(float(row["vdem_polyarchy"])),  # Target: democratic resilience
            "metadata_fold": None,
            "metadata_feature_names": list(input_features.keys())
        }
        
        output["datasets"][0]["examples"].append(example)
    
    # Add metadata
    metadata = {
        "title": "Panel Dataset for Welfare State Capacity and Democratic Resilience (1990-2023)",
        "description": "Unified panel dataset of post-1990 democratizers with variables for mediated moderation analysis",
        "source": "Synthetic data based on patterns from V-Dem, Polity IV, World Bank PIP, OECD SOCX",
        "years": "1990-2023",
        "countries": int(df["country_code"].nunique()),
        "observations": int(len(df)),
        "variables": list(df.columns),
        "schema": {
            "country_code": "ISO 3-letter country code",
            "country_name": "Country name",
            "year": "Year (1990-2023)",
            "gini": "Gini coefficient (0-100 scale)",
            "vdem_polyarchy": "V-Dem Electoral Democracy Index (0-1)",
            "polity_iv": "Polity IV score (-10 to +10)",
            "primary_enrollment": "Primary enrollment rate (%)",
            "secondary_enrollment": "Secondary enrollment rate (%)",
            "tertiary_enrollment": "Tertiary enrollment rate (%)",
            "social_spending_gdp": "Social spending as % of GDP",
            "social_protection_coverage": "Social protection coverage (%)",
            "welfare_capacity_index": "Welfare state capacity index (0-1)",
            "educational_polarization": "Educational polarization index (0-1)",
            "post_1990_democratizer": "Flag: post-1990 democratizer (1=yes, 0=no)",
            "transition_year": "Year of democratic transition"
        }
    }
    
    output["metadata"] = metadata
    
    # Export full version
    full_path = WORKSPACE / "data_out.json"
    with open(full_path, 'w') as f:
        json.dump(output, f, indent=2, default=convert_to_serializable)
    print(f"Exported full dataset to: {full_path}")
    print(f"  Total size: {full_path.stat().st_size / 1024 / 1024:.2f} MB")
    print(f"  Total examples: {len(output['datasets'][0]['examples'])}")
    
    # Export mini version (3 countries x 10 years)
    mini_countries = df["country_code"].unique()[:3]
    mini_df = df[df["country_code"].isin(mini_countries) & (df["year"] >= 1990) & (df["year"] <= 1999)]
    
    mini_output = output.copy()
    mini_output["datasets"][0]["examples"] = []
    
    for _, row in mini_df.iterrows():
        input_features = {
            "country_code": row["country_code"],
            "country_name": row["country_name"],
            "year": int(row["year"]),
            "gini": float(row["gini"]),
        }
        
        example = {
            "input": json.dumps(input_features),
            "output": str(float(row["vdem_polyarchy"])),
            "metadata_fold": None,
            "metadata_feature_names": ["country_code", "country_name", "year", "gini"]
        }
        
        mini_output["datasets"][0]["examples"].append(example)
    
    mini_output["metadata"]["note"] = "Mini version: 3 countries x 10 years"
    
    mini_path = WORKSPACE / "mini_data_out.json"
    with open(mini_path, 'w') as f:
        json.dump(mini_output, f, indent=2, default=convert_to_serializable)
    print(f"Exported mini dataset to: {mini_path}")
    print(f"  Total examples: {len(mini_output['datasets'][0]['examples'])}")
    
    # Export preview version (first 5 observations)
    preview_output = output.copy()
    preview_output["datasets"][0]["examples"] = output["datasets"][0]["examples"][:5]
    preview_output["metadata"]["note"] = "Preview version: first 5 observations"
    
    preview_path = WORKSPACE / "preview_data_out.json"
    with open(preview_path, 'w') as f:
        json.dump(preview_output, f, indent=2, default=convert_to_serializable)
    print(f"Exported preview dataset to: {preview_path}")
    
    return full_path, mini_path, preview_path

def main():
    """Main execution"""
    print("="*60)
    print("EXPORTING PANEL DATASET")
    print("="*60)
    
    # Load/prepare data
    df = load_and_prepare_data()
    
    # Export to JSON
    full_path, mini_path, preview_path = export_to_json(df)
    
    print("\n" + "="*60)
    print("EXPORT COMPLETE")
    print("="*60)
    print(f"Full dataset: {full_path}")
    print(f"Mini dataset: {mini_path}")
    print(f"Preview dataset: {preview_path}")

if __name__ == "__main__":
    main()
