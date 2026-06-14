#!/usr/bin/env -S uv run --quiet
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas",
#     "loguru",
# ]
# ///

"""Convert panel dataset to experiment pipeline format."""

from loguru import logger
from pathlib import Path
import json
import sys
import pandas as pd

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load the panel dataset
    input_file = Path("temp/datasets/panel_data_out.csv")
    output_dir = Path(".")
    
    logger.info(f"Loading panel dataset from {input_file}")
    df = pd.read_csv(input_file)
    logger.info(f"Loaded {len(df)} rows, {df.shape[1]} columns")
    
    # Define feature columns (inputs)
    feature_cols = [
        'democracy_polity',
        'regime_polity', 
        'democracy_eiu',
        'regime_eiu',
        'inequality_gini',
        'welfare_capacity_gdp_share',
        'educ_polarization_gini',
        'post_1990_democratizer',
        'post_transition'
    ]
    
    # Filter to columns that exist
    feature_cols = [col for col in feature_cols if col in df.columns]
    logger.info(f"Feature columns: {feature_cols}")
    
    # Create examples
    # For this panel dataset, each row is an example
    # Input: feature values as JSON string
    # Output: country-year identifier (or we could predict democratic resilience)
    
    # Define output column - using democracy_polity as target (democratic resilience)
    output_col = 'democracy_polity'
    if output_col not in df.columns:
        # Fallback: use regime_polity
        output_col = 'regime_polity' if 'regime_polity' in df.columns else None
    
    examples = []
    for idx, row in df.iterrows():
        # Skip rows with too many missing values
        feature_values = {col: row[col] for col in feature_cols}
        non_null_count = sum(1 for v in feature_values.values() if pd.notna(v))
        
        if non_null_count < len(feature_cols) * 0.5:  # Less than 50% non-null
            continue
        
        # Create input as JSON string of features
        input_dict = {col: float(row[col]) if pd.notna(row[col]) else None for col in feature_cols}
        input_str = json.dumps(input_dict)
        
        # Create output
        if output_col and pd.notna(row[output_col]):
            output_val = str(float(row[output_col]))
        else:
            output_val = "unknown"
        
        example = {
            "input": input_str,
            "output": output_val,
            "metadata_fold": hash(row['country']) % 5,  # 5-fold CV based on country
            "metadata_feature_names": feature_cols,
            "metadata_task_type": "regression",
            "metadata_n_classes": None,
            "metadata_row_index": int(idx),
            "metadata_country": row['country'],
            "metadata_year": int(row['year']) if pd.notna(row['year']) else None
        }
        examples.append(example)
    
    logger.info(f"Created {len(examples)} examples")
    
    # Create output structure
    output_data = {
        "datasets": [
            {
                "dataset": "welfare_state_democracy_panel_1990_2023",
                "examples": examples
            }
        ]
    }
    
    # Save to full_data_out.json
    output_file = output_dir / "full_data_out.json"
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    logger.info(f"Saved {len(examples)} examples to {output_file}")
    
    # Also save a summary
    summary = {
        "dataset_name": "welfare_state_democracy_panel_1990_2023",
        "n_examples": len(examples),
        "n_features": len(feature_cols),
        "feature_columns": feature_cols,
        "output_column": output_col,
        "task_type": "regression",
        "years_covered": f"{int(df['year'].min())}-{int(df['year'].max())}",
        "countries": df['country'].nunique(),
        "missing_data_pct": {
            col: (df[col].isna().sum() / len(df) * 100) for col in feature_cols + ([output_col] if output_col else [])
        }
    }
    
    summary_file = output_dir / "dataset_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    logger.info(f"Saved summary to {summary_file}")
    
    logger.info("Data conversion completed!")

if __name__ == "__main__":
    main()
