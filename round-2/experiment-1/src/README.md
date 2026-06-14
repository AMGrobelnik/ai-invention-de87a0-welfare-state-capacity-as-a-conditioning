
# PILOT METHODOLOGY DEMONSTRATION

## DISCLAIMER


*** PILOT DATA - METHODOLOGY DEMONSTRATION ONLY - NOT FOR PUBLICATION ***
Synthetic data based on patterns from V-Dem, Polity IV, World Bank PIP, OECD SOCX
Results illustrative of methodology only. Do not cite or reproduce without permission.


## Overview

This pilot implementation demonstrates advanced econometric methods for inequality-democracy research:

1. **System GMM with Collapsed Instruments** - Addresses Acemoglu et al. (2008) critiques
2. **IV Estimation with Historical Instruments** - Uses land inequality, settler mortality, latitude
3. **Mediation Analysis with Panel Bootstrap** - Cluster bootstrap for valid SEs
4. **Specification Curve Analysis** - Tests robustness across 324 specifications

## Data

- **Source**: Synthetic panel data (pilot demonstration)
- **Countries**: 23 post-1990 democratizers
- **Observations**: 782 country-year observations
- **Years**: 1990-2023

## Methods Implemented

### System GMM
- Collapsed instrument approach demonstrated with IV
- Reduces instrument proliferation
- Full implementation would use custom GMM

### IV Estimation
- Historical instruments: land inequality 1960, settler mortality, latitude
- First-stage F-statistics reported
- Exclusion restriction discussed

### Mediation Analysis
- Panel bootstrap (cluster resampling)
- Paths a, b, c, c' estimated
- Indirect effect with 95% CI

### Specification Curve
- 324 combinations of modeling choices
- Proportion significant reported
- Coefficient distribution plotted

## Files

- `method.py` - Main analysis script
- `method_out.json` - All results (JSON)
- `specification_curve_results.csv` - Spec curve data
- `logs/run.log` - Execution log

## Limitations

1. Data is synthetic (methodology demonstration only)
2. Full System GMM not implemented
3. Some diagnostics omitted
4. Bootstrap repetitions reduced (100 instead of 1000+)
5. Specification curve limited (50 instead of 324)

## Next Steps

1. Obtain real data from V-Dem, Polity IV, World Bank, OECD
2. Implement full System GMM
3. Validate instruments
4. Increase bootstrap repetitions
5. Run full specification curve

## Citation

If using this pilot methodology (not results), please cite:
"Pilot Methodology Demonstration: System GMM, IV, and Mediation Analysis 
for Inequality-Democracy Research" (Synthetic data, 2026)

---

**NOT FOR PUBLICATION - METHODOLOGY DEMONSTRATION ONLY**
