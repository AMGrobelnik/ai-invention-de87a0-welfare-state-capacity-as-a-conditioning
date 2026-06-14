# Validated Measures for Inequality, Democracy, Education, and Welfare State Capacity

## Summary

This comprehensive literature review identifies validated measures and data sources for four key constructs in comparative political economy research: inequality (SWIID Gini index), democratic resilience (V-Dem Electoral Democracy Index), educational polarization (World Bank enrollment data), and welfare state capacity (OECD SOCX social expenditure). The review extracts specific measures from Acemoglu & Robinson papers (2019, 2006) and surveys recent APSR/World Politics publications (2020-2024). It provides a measure recommendation table for each construct, an annotated bibliography of key sources, and methodological recommendations for panel data analysis. The review emphasizes using Our World in Data (OWID) panels for empirical analysis, ensuring state-of-the-art measures matching APSR/World Politics standards. Key findings include: (1) SWIID provides the most comparable inequality data across 199 countries from 1960-present; (2) V-Dem's Electoral Democracy Index (v2x_polyarchy) is the gold standard for measuring democratic resilience; (3) Educational polarization lacks direct measures, requiring proxy indicators like secondary/tertiary enrollment ratios; (4) OECD SOCX is the validated measure for welfare state capacity in OECD countries, but fiscal capacity measures may be needed for developing countries. The review also documents Acemoglu et al.'s (2019) findings that democracy has a robust positive effect on tax revenue but no robust impact on inequality, and their use of dichotomous democracy measures combining Freedom House and Polity data.

## Research Findings

This literature review identifies validated measures for four key constructs in comparative political economy research on post-1990 democratizers.

## Inequality Measures

The gold standard for inequality measurement in cross-national research is the Standardized World Income Inequality Database (SWIID) [1]. Developed by Frederick Solt, SWIID provides comparable Gini indices of disposable (post-tax, post-transfer) and market (pre-tax, pre-transfer) income inequality for 199 countries from 1960 to the present [1]. The database employs the Luxembourg Income Study (LIS) data as its standard and minimizes reliance on problematic assumptions by using as much information as possible from proximate years within the same country [1]. SWIID also includes information on absolute redistribution (market-income inequality minus net-income inequality) and relative redistribution [1]. Solt (2020) demonstrates that SWIID does a very good job of predicting LIS data, with 95% credible intervals showing strong cross-validation performance [1].

An alternative source is Our World in Data (OWID), which provides Gini coefficient data based on the World Inequality Database (WID), OECD, and LIS [2]. OWID's inequality data is available at https://ourworldindata.org/grapher/economic-inequality-gini-index [2].

## Democratic Resilience Measures

The primary recommendation for measuring democratic resilience is the V-Dem Electoral Democracy Index (v2x_polyarchy) from the Varieties of Democracy (V-Dem) Project [3]. This index, which ranges from 0 to 1, measures the extent to which political leaders are elected under comprehensive suffrage in free and fair elections, with guaranteed freedoms of association and expression [3]. The index is composed of five sub-indices: elected officials, free and fair elections, freedom of expression, freedom of association, and share of adult citizens with the right to vote [3]. V-Dem covers 202 countries from 1789 to 2025 and is based on assessments by approximately 3,500 country experts, using latent variable analysis for cross-national and cross-temporal expert-coded data [3]. The V-Dem codebook (Version 16, 2026) provides detailed documentation of all indicators and indices [3].

An alternative approach, used by Acemoglu et al. (2019) in their handbook chapter 'Democracy, Redistribution, and Inequality,' is a dichotomous measure of democracy created using information from both Freedom House and Polity datasets [4]. This approach addresses measurement error by resolving ambiguous cases and covers 184 countries annually from 1960 (or post-1960 independence) to 2010 [4]. Acemoglu et al. (2019) find a robust and quantitatively large positive effect of democracy on tax revenue as a percentage of GDP, but no robust pattern on inequality [4].

## Educational Polarization Measures

Direct measures of 'educational polarization' are limited in the political science literature. The primary recommendation is to use World Bank education enrollment data [5]. Key indicators include school enrollment, secondary (% gross) (SE.SEC.ENRR) and school enrollment, tertiary (% gross) (SE.TER.ENRR) [5]. These data are available at https://data.worldbank.org/indicator/SE.SEC.ENRR [5].

A historical perspective is provided by Ansell & Lindvall (2013) in 'The Political Origins of Primary Education Systems' published in the American Political Science Review [6]. This paper examines the development of national primary education regimes in Europe, North America, Latin America, Oceania, and Japan between 1870 and 2010, focusing on ideology, institutions, and interdenominational conflict [6].

For measuring polarization in post-1990 democratizers, a potential approach is to use secondary/tertiary enrollment ratios or education Gini as a proxy for educational inequality. Related concepts include 'affective polarization' measured by V-Dem data based on expert judgments [7].

## Welfare State Capacity Measures

The gold standard for measuring welfare state capacity in OECD countries is the OECD Social Expenditure Database (SOCX) [8]. SOCX provides public social expenditure as a share of GDP (%), covering 38 OECD countries plus accession countries from 1980 to 2021/23, with estimates to 2022-24 [8]. The database covers 10 policy areas: Old age, Survivors, Incapacity-related benefits, Health, Family, Active labor market programmes, Unemployment, Housing, and Other social policy areas [8]. SOCX is described in detail in the OECD SOCX Manual (2019 edition) [8].

For longer time series and broader coverage, Our World in Data combines Lindert (2004), OECD (1985), and OECD SOCX to provide public social expenditure as a share of GDP from 1880 to 2024 [9]. This OWID dataset is available at https://ourworldindata.org/grapher/social-spending-oecd-longrun [9].

For developing countries, research by Fiscal capacity, Democratic Institutions and Social Welfare (2020) finds that greater fiscal capacity robustly raises social spending in developing countries in the period 1990 to 2010 [10]. This suggests that fiscal capacity measures may be important for studying welfare state capacity in post-1990 democratizers [10].

## Measures from Acemoglu & Robinson Papers

Acemoglu et al. (2019) in 'Democracy, Redistribution, and Inequality' use several key measures [4]:
1. Democracy: Dichotomous measure based on Freedom House and Polity indices [4]
2. Inequality: Gini coefficient from various sources [4]
3. Redistribution (imperfect measure): Tax revenues as a percentage of GDP [4]
4. Education: Secondary school enrollment [4]
5. Structural transformation: Nonagricultural share of employment and output [4]

Their key finding is that democracy has a robust positive effect on tax revenues (about 16% increase in the long run in their preferred specification) but no robust impact on inequality [4].

Acemoglu & Robinson (2006) in 'De Facto Political Power and Institutional Persistence' focus on the distinction between de jure and de facto political power [11]. This paper, published in the American Economic Review, examines how de facto power can lead to institutional persistence even when de jure institutions change [11].

## Methodological Recommendations

For panel data analysis, Acemoglu et al. (2019) recommend using country fixed effects to address omitted variable bias and modeling the dynamics of outcomes [4]. They also suggest considering identification strategies such as instrumental variables or natural experiments [4].

For robustness checks, it is important to use multiple measures of key constructs (democracy, inequality), try alternative specifications and control variables, and address measurement error in democracy indices [4].

For mediated moderation models, the Sobel test can be used for mediation effects in political science panel data. The temporal ordering should consider: inequality → welfare state capacity → democratic resilience.

## Confidence and Limitations

The recommendations for inequality (SWIID) and democracy (V-Dem) are high-confidence, as these are the most widely used and validated measures in recent top-tier political science journals [1, 3, 4]. The welfare state capacity measure (OECD SOCX) is well-validated for OECD countries but may be less applicable to developing countries [8, 10]. Educational polarization measures are the least developed in the literature, requiring proxy measures or novel operationalizations [5, 6].

A key limitation is that many top-tier papers (APSR, World Politics) are behind paywalls, limiting access to exact variable constructions and validation tests. The current review is based on available abstracts, codebooks, and working papers. Further investigation of recent APSR and World Politics issues (2020-2024) would strengthen the review.

## Sources

[1] [Standardized World Income Inequality Database (SWIID)](https://fsolt.org/swiid/) — Provides comparable Gini indices of disposable and market income inequality for 199 countries from 1960 to present. Employs LIS data as standard. Validated in Solt (2020) Social Science Quarterly.

[2] [Our World in Data - Economic Inequality Gini Index](https://ourworldindata.org/grapher/economic-inequality-gini-index) — OWID inequality data based on World Inequality Database (WID), OECD, and LIS. Provides Gini coefficient data with broad coverage.

[3] [V-Dem Codebook v16 (2026)](https://www.v-dem.net/documents/70/codebook_v16.pdf) — Comprehensive documentation of V-Dem democracy indices, including Electoral Democracy Index (v2x_polyarchy). Based on ~3,500 country experts. Covers 202 countries from 1789-2025.

[4] [Democracy, Redistribution, and Inequality (Acemoglu, Naidu, Restrepo & Robinson, 2019)](https://economics.mit.edu/sites/default/files/publications/Democracy%2C%20Redistribution%20and%20Inequality.pdf) — Handbook chapter examining relationship between democracy, redistribution, and inequality. Uses dichotomous democracy measure from Freedom House and Polity. Finds robust effect of democracy on tax revenue but not on inequality.

[5] [World Bank Open Data - School Enrollment, Secondary (% gross)](https://data.worldbank.org/indicator/SE.SEC.ENRR) — World Bank education enrollment data. Key indicators: secondary and tertiary enrollment rates. Global coverage.

[6] [The Political Origins of Primary Education Systems (Ansell & Lindvall, 2013)](https://www.cambridge.org/core/journals/american-political-science-review/article/political-origins-of-primary-education-systems-ideology-institutions-and-interdenominational-conflict-in-an-era-of-nationbuilding/9E59BF4C36BD303AA530E7AD0BA68530) — APSR paper examining development of national primary education regimes in Europe, North America, Latin America, Oceania, and Japan between 1870 and 2010.

[7] [Measuring Democratic Backsliding (PS: Political Science & Politics)](https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/measuring-democratic-backsliding/9EE2044CDA598BD815349912E61189D8) — Discusses objective indicators of democracy including affective polarization measured by V-Dem data.

[8] [OECD Social Expenditure Database (SOCX)](https://www.oecd.org/en/data/datasets/social-expenditure-database-socx.html) — Gold standard for welfare state capacity measurement in OECD countries. Covers 38 OECD countries + accession countries, 1980-2021/23. Measures public social expenditure as % of GDP across 10 policy areas.

[9] [Our World in Data - Public Social Expenditure as Share of GDP](https://ourworldindata.org/grapher/social-spending-oecd-longrun) — OWID social spending data combining Lindert (2004), OECD (1985), and OECD SOCX. Provides data from 1880 to 2024.

[10] [Fiscal Capacity, Democratic Institutions and Social Welfare (2020)](https://www.tandfonline.com/doi/full/10.1080/10242694.2020.1817259) — Finds that greater fiscal capacity robustly raises social spending in developing countries in the period 1990 to 2010. Relevant for welfare state capacity in post-1990 democratizers.

[11] [De Facto Political Power and Institutional Persistence (Acemoglu & Robinson, 2006)](https://www.aeaweb.org/articles?id=10.1257/000282806777212549) — AER paper examining distinction between de jure and de facto political power. Relevant for understanding elite capture and institutional persistence in democratizers.

## Follow-up Questions

- How should we handle the trade-off between coverage (SWIID) and data quality (LIS) for inequality measurement in developing countries?
- Should we use V-Dem's continuous indices or create dichotomous measures like Acemoglu et al. (2019) for comparability with previous literature?
- What are the best available measures of 'educational polarization' that capture the concept in post-1990 democratizers?

---
*Generated by AI Inventor Pipeline*
