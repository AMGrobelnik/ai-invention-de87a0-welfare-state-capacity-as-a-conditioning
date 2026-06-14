# Literature Review Findings: Measures for Inequality, Democracy, Education, and Welfare State Capacity

## 1. INEQUALITY MEASURES

### Primary Recommendation: SWIID (Standardized World Income Inequality Database)
- **Source**: Frederick Solt, Version 9.92 (April 2026) [1]
- **Measure**: Gini indices of disposable (post-tax, post-transfer) and market (pre-tax, pre-transfer) income inequality
- **Coverage**: 199 countries from 1960 to present
- **Validation**: Employs Luxembourg Income Study (LIS) data as standard; minimizes reliance on problematic assumptions [1]
- **Additional measures**: Absolute redistribution (market-income inequality minus net-income inequality) and relative redistribution [1]
- **Citation**: Solt, Frederick. 2020. "Measuring Income Inequality Across Countries and Over Time: The Standardized World Income Inequality Database." Social Science Quarterly 101(3):1183-1199.

### Alternative: Our World in Data (OWID) Inequality Data
- **Source**: OWID based on World Inequality Database (WID), OECD, and LIS [2]
- **Measure**: Gini coefficient (0-1 scale)
- **URL**: https://ourworldindata.org/grapher/economic-inequality-gini-index [2]

## 2. DEMOCRATIC RESILIENCE MEASURES

### Primary Recommendation: V-Dem Electoral Democracy Index (v2x_polyarchy)
- **Source**: Varieties of Democracy (V-Dem) Project, Version 16 (2026) [3]
- **Measure**: Index (0-1 scale) measuring extent to which political leaders are elected under comprehensive suffrage in free and fair elections, with freedoms of association and expression guaranteed [3]
- **Components**: 5 sub-indices: elected officials, free and fair elections, freedom of expression, freedom of association, and share of adult citizens with right to vote [3]
- **Coverage**: 202 countries from 1789-2025
- **Validation**: Based on assessments by ~3,500 country experts; uses latent variable analysis for cross-national and cross-temporal expert-coded data [3]
- **Citation**: Coppedge et al. 2026. "V-Dem [Country-Year/Country-Date] Dataset v16" Varieties of Democracy (V-Dem) Project.

### Alternative: Polity IV and Freedom House (used by Acemoglu et al. 2019)
- **Source**: Acemoglu, Naidu, Restrepo & Robinson (2019) [4]
- **Measure**: Dichotomous measure of democracy created using information from both Freedom House and Polity datasets [4]
- **Validation**: Addresses measurement error by resolving ambiguous cases [4]
- **Coverage**: 184 countries annually from 1960 (or post-1960 independence) to 2010 [4]

## 3. EDUCATIONAL POLARIZATION MEASURES

### Primary Recommendation: World Bank Education Enrollment Data
- **Source**: World Bank Open Data [5]
- **Measures**: 
  - School enrollment, secondary (% gross) - SE.SEC.ENRR [5]
  - School enrollment, tertiary (% gross) - SE.TER.ENRR [5]
- **URL**: https://data.worldbank.org/indicator/SE.SEC.ENRR [5]

### Alternative: Ansell & Lindvall (2013) Measures
- **Source**: Ansell, Ben & Lindvall, Johannes. 2013. "The Political Origins of Primary Education Systems." American Political Science Review 107(3):505-522. [6]
- **Focus**: Primary education systems, ideology, institutions, and interdenominational conflict [6]
- **Relevance**: Historical perspective on education policy and democracy [6]

### Note on Educational Polarization
- Limited direct measures of "educational polarization" in political science literature
- Related concept: "Affective polarization" measured by V-Dem data based on expert judgments [7]
- Suggestion: Use secondary/tertiary enrollment ratios or education Gini as proxy for educational inequality

## 4. WELFARE STATE CAPACITY MEASURES

### Primary Recommendation: OECD Social Expenditure Database (SOCX)
- **Source**: OECD Social Expenditure Database (SOCX) [8]
- **Measure**: Public social expenditure as share of GDP (%) [8]
- **Coverage**: 38 OECD countries + accession countries, 1980-2021/23, estimates to 2022-24 [8]
- **Policy areas**: Old age, Survivors, Incapacity-related benefits, Health, Family, Active labor market programmes, Unemployment, Housing, Other [8]
- **URL**: https://www.oecd.org/en/data/datasets/social-expenditure-database-socx.html [8]

### Alternative: OWID Social Spending Data
- **Source**: Our World in Data combining Lindert (2004), OECD (1985), and OECD SOCX [9]
- **Measure**: Public social expenditure as share of GDP (%) [9]
- **Time coverage**: 1880-2024 (extended series) [9]
- **URL**: https://ourworldindata.org/grapher/social-spending-oecd-longrun [9]

### For Developing Countries:
- **Source**: Fiscal capacity and social spending in developing countries (1990-2010) [10]
- **Finding**: Greater fiscal capacity robustly raises social spending in developing countries [10]
- **Citation**: Available at https://www.tandfonline.com/doi/full/10.1080/10242694.2020.1817259 [10]

## 5. ADDITIONAL MEASURES FROM Acemoglu & Robinson PAPERS

### Acemoglu et al. (2019) - "Democracy, Redistribution, and Inequality"
- **Democracy measure**: Dichotomous measure based on Freedom House and Polity indices [4]
- **Inequality measure**: Gini coefficient (various sources) [4]
- **Tax revenue measure**: Tax revenues as percentage of GDP (imperfect measure of redistribution) [4]
- **Secondary education measure**: Secondary school enrollment [4]
- **Structural transformation measures**: Nonagricultural share of employment and output [4]
- **Key finding**: Robust positive effect of democracy on tax revenue (16% increase long-run), but no robust pattern on inequality [4]

### Acemoglu & Robinson (2006) - "De Facto Political Power and Institutional Persistence"
- **Focus**: De facto political power vs. de jure political institutions [11]
- **Relevance**: Elite capture and institutional persistence [11]
- **Citation**: Acemoglu, Daron, and James A. Robinson. 2006. "De Facto Political Power and Institutional Persistence." American Economic Review 96(2): 325-330. [11]

## 6. METHODOLOGICAL RECOMMENDATIONS

### Panel Data Approaches:
- Use country fixed effects to address omitted variable bias [4]
- Model dynamics of outcomes (taxes, inequality, etc.) [4]
- Consider identification strategies (instrumental variables, natural experiments) [4]

### Robustness Checks:
- Multiple measures of key constructs (democracy, inequality) [4]
- Alternative specifications and control variables [4]
- Address measurement error in democracy indices [4]

### Mediated Moderation:
- Sobel test for mediation effects in political science panel data
- Consider temporal ordering: inequality → welfare state capacity → democratic resilience

## 7. DATA SOURCES SUMMARY TABLE

| Construct | Primary Measure | Data Source | Coverage | Citation |
|-----------|-----------------|-------------|----------|----------|
| Inequality | Gini index (disposable income) | SWIID v9.92 | 199 countries, 1960-present | Solt (2020) [1] |
| Democracy | Electoral Democracy Index | V-Dem v16 | 202 countries, 1789-2025 | Coppedge et al. (2026) [3] |
| Education | Secondary enrollment (%) | World Bank | Global | World Bank [5] |
| Welfare capacity | Social expenditure (% GDP) | OECD SOCX | 38 OECD + accession | OECD [8] |
| Redistribution | Tax revenue (% GDP) | World Bank | Global | World Bank |

## 8. ANNOTATED BIBLIOGRAPHY

1. **Solt (2020)** - SWIID: Maximizes comparability of income inequality data while maintaining widest possible coverage. Uses LIS as standard. Provides Gini indices for 199 countries from 1960.

2. **Coppedge et al. (2026)** - V-Dem v16: Comprehensive democracy ratings covering electoral, liberal, participatory, deliberative, and egalitarian democracy. Based on ~3,500 country experts.

3. **Acemoglu et al. (2019)** - "Democracy, Redistribution, and Inequality": Finds robust effect of democracy on tax revenue but not on inequality. Uses dichotomous democracy measure from Freedom House and Polity.

4. **Ansell & Lindvall (2013)** - "The Political Origins of Primary Education Systems": Examines development of national primary education regimes in Europe, North America, Latin America, Oceania, and Japan between 1870 and 2010.

5. **OECD SOCX** - Standardized social expenditure data covering 10 policy areas. Gold standard for welfare state capacity measurement in OECD countries.

## 9. FOLLOW-UP QUESTIONS

1. How should we handle the trade-off between coverage (SWIID) and data quality (LIS) for inequality measurement in developing countries?

2. Should we use V-Dem's continuous indices or create dichotomous measures like Acemoglu et al. (2019) for comparability with previous literature?

3. What are the best available measures of "educational polarization" that capture the concept in post-1990 democratizers?

4. How can we measure "welfare state capacity" in developing countries where OECD SOCX data is not available?
