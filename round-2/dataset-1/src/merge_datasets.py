#!/usr/bin/env python3
"""Merge collected datasets for welfare state capacity research."""
import json
import pandas as pd
from pathlib import Path

def main():
    # Create output directory
    output_dir = Path("temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load datasets from OWID temp/tables directory
    owid_dir = Path("/home/adrian/projects/ai-inventor/.claude/skills/aii-owid-datasets/temp/tables")
    
    print("Loading datasets...")
    
    # 1. Load Polity IV data (base dataset)
    polity_file = owid_dir / "full_garden_democracy_2024-03-07_polity_polity.json"
    if polity_file.exists():
        with open(polity_file, "r") as f:
            data = json.load(f)
        df_polity = pd.DataFrame(data)
        print(f"Loaded Polity data: {len(df_polity)} rows")
        print(f"Polity columns: {df_polity.columns.tolist()}")
    else:
        print("Polity data not found")
        return
    
    # Create base dataset with years 1990-2023
    df_polity['year'] = pd.to_numeric(df_polity['year'], errors='coerce')
    df_base = df_polity[(df_polity['year'] >= 1990) & (df_polity['year'] <= 2023)].copy()
    print(f"Base dataset (Polity 1990-2023): {len(df_base)} rows")
    
    # 2. Load EIU democracy index
    eiu_file = owid_dir / "full_garden_democracy_2024-03-07_eiu_eiu.json"
    if eiu_file.exists():
        with open(eiu_file, "r") as f:
            data = json.load(f)
        df_eiu = pd.DataFrame(data)
        df_eiu['year'] = pd.to_numeric(df_eiu['year'], errors='coerce')
        df_base = df_base.merge(
            df_eiu[['country', 'year', 'democracy_eiu', 'regime_eiu']], 
            on=['country', 'year'], 
            how='left'
        )
        print("Merged EIU democracy index")
    
    # 3. Load WIID (inequality data)
    wiid_file = owid_dir / "full_garden_unu_wider_2024-04-22_world_income_inequality_database_world_income_inequa.json"
    if wiid_file.exists():
        with open(wiid_file, "r") as f:
            data = json.load(f)
        df_wiid = pd.DataFrame(data)
        df_wiid['year'] = pd.to_numeric(df_wiid['year'], errors='coerce')
        
        # Get the Gini column
        gini_col = [col for col in df_wiid.columns if 'gini' in col.lower()]
        if gini_col:
            df_wiid_subset = df_wiid[['country', 'year', gini_col[0]]].copy()
            df_wiid_subset = df_wiid_subset.rename(columns={gini_col[0]: 'inequality_gini'})
            df_base = df_base.merge(
                df_wiid_subset,
                on=['country', 'year'],
                how='left'
            )
            print("Merged WIID inequality data")
    
    # 4. Load OECD Social Expenditure Dataset
    oecd_file = owid_dir / "full_garden_oecd_2025-02-25_social_expenditure_social_expenditure.json"
    if oecd_file.exists():
        with open(oecd_file, "r") as f:
            data = json.load(f)
        df_oecd = pd.DataFrame(data)
        df_oecd['year'] = pd.to_numeric(df_oecd['year'], errors='coerce')
        
        # Filter for total social expenditure as % of GDP
        df_oecd_subset = df_oecd[
            (df_oecd['programme_type_category'] == 'All') & 
            (df_oecd['programme_type'] == 'Total')
        ][['country', 'year', 'share_gdp']].copy()
        df_oecd_subset = df_oecd_subset.rename(columns={'share_gdp': 'welfare_capacity_gdp_share'})
        df_base = df_base.merge(
            df_oecd_subset,
            on=['country', 'year'],
            how='left'
        )
        print("Merged OECD social expenditure data")
    
    # 5. Load Clio-Infra education data
    education_file = owid_dir / "full_garden_education_2023-08-09_clio_infra_education_clio_infra_education.json"
    if education_file.exists():
        with open(education_file, "r") as f:
            data = json.load(f)
        df_education = pd.DataFrame(data)
        df_education['year'] = pd.to_numeric(df_education['year'], errors='coerce')
        
        if 'years_of_education_gini' in df_education.columns:
            df_edu_subset = df_education[['country', 'year', 'years_of_education_gini']].copy()
            df_edu_subset = df_edu_subset.rename(columns={'years_of_education_gini': 'educ_polarization_gini'})
            df_base = df_base.merge(
                df_edu_subset,
                on=['country', 'year'],
                how='left'
            )
            print("Merged education inequality data")
    
    # Identify post-1990 democratizers
    print("Identifying post-1990 democratizers...")
    if 'democracy_polity' in df_base.columns:
        df_base = df_base.sort_values(['country', 'year'])
        
        # Mark democratizers: autocracy before 1990, democracy after 1990
        def check_democracy_before(group):
            pre_1990 = group[group['year'] < 1990]
            if len(pre_1990) > 0:
                return (pre_1990['democracy_polity'] < -5).any()
            return False
        
        def check_democracy_after(group):
            post_1990 = group[group['year'] >= 1990]
            if len(post_1990) > 0:
                return (post_1990['democracy_polity'] > 5).any()
            return False
        
        democracy_before = df_base.groupby('country').apply(check_democracy_before)
        democracy_after = df_base.groupby('country').apply(check_democracy_after)
        
        df_base['post_1990_democratizer'] = df_base['country'].map(democracy_before) & df_base['country'].map(democracy_after)
        
        # Get transition year (first year with democracy_polity > 5 after 1990)
        def get_transition_year(group):
            democratic = group[group['democracy_polity'] > 5]
            if len(democratic) > 0:
                return democratic['year'].min()
            return float('nan')
        
        transition_years = df_base.groupby('country').apply(get_transition_year)
        df_base['transition_year'] = df_base['country'].map(transition_years)
        df_base['post_transition'] = df_base['year'] >= df_base['transition_year']
        
        print(f"Identified {df_base['post_1990_democratizer'].sum()} post-1990 democratizer country-years")
    
    # Select final columns
    final_cols = [
        'country', 'year', 'post_1990_democratizer', 'transition_year', 'post_transition',
        'democracy_polity', 'regime_polity', 'democracy_eiu', 'regime_eiu',
        'inequality_gini', 'welfare_capacity_gdp_share', 'educ_polarization_gini'
    ]
    final_cols = [col for col in final_cols if col in df_base.columns]
    
    df_final = df_base[final_cols].copy()
    
    # Generate summary statistics
    print("=== SUMMARY STATISTICS ===")
    print(f"Total observations: {len(df_final)}")
    print(f"Countries: {df_final['country'].nunique()}")
    print(f"Years: {df_final['year'].min()} - {df_final['year'].max()}")
    
    for col in df_final.columns:
        if col not in ['country', 'year', 'post_1990_democratizer', 'post_transition']:
            non_null = df_final[col].notna().sum()
            pct_missing = (1 - non_null / len(df_final)) * 100
            print(f"{col}: {non_null} non-null, {pct_missing:.1f}% missing")
    
    # Save output
    output_file = output_dir / "panel_data_out.json"
    df_final.to_json(output_file, orient='records', indent=2)
    print(f"Saved panel dataset to {output_file}")
    
    # Also save as CSV for readability
    csv_file = output_dir / "panel_data_out.csv"
    df_final.to_csv(csv_file, index=False)
    print(f"Saved panel dataset to {csv_file}")
    
    # Create codebook
    codebook = {
        "dataset_description": "Panel dataset for welfare state capacity and democratic resilience research (1990-2023)",
        "sources": {
            "polity": "Polity IV Project - Political Regime Characteristics and Transitions",
            "eiu": "Economist Intelligence Unit Democracy Index",
            "wiid": "World Income Inequality Database (UNU-WIDER)",
            "oecd": "OECD Social Expenditure Database (SOCX)",
            "education": "Clio-Infra Historical Education Inequality Data"
        },
        "variables": {
            "country": "Country name",
            "year": "Year (1990-2023)",
            "post_1990_democratizer": "Binary flag: 1 if country transitioned from autocracy to democracy after 1990",
            "transition_year": "Year of democratic transition (first year with Polity democracy score > 5)",
            "post_transition": "Binary flag: 1 if year is after transition year",
            "democracy_polity": "Polity IV democracy score (-10 to +10)",
            "regime_polity": "Polity IV regime type (0=autocracy, 1=anocracy, 2=democracy)",
            "democracy_eiu": "EIU democracy index score (0-10)",
            "regime_eiu": "EIU regime type (0=authoritarian, 1=hybrid, 2=flawed democracy, 3=full democracy)",
            "inequality_gini": "Gini coefficient for income inequality (0-100 scale)",
            "welfare_capacity_gdp_share": "Social expenditure as share of GDP (%)",
            "educ_polarization_gini": "Educational inequality Gini coefficient"
        }
    }
    
    codebook_file = output_dir / "codebook.json"
    with open(codebook_file, "w") as f:
        json.dump(codebook, f, indent=2)
    print(f"Saved codebook to {codebook_file}")
    
    print("Dataset creation completed!")

if __name__ == "__main__":
    main()
