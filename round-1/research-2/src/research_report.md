# Identification Strategy for Mediated Moderation: Inequality, Education, Welfare

## Summary

This research artifact provides a comprehensive identification strategy for estimating a mediated moderation model examining how welfare state capacity moderates the inequality→educational polarization→democratic resilience pathway in post-1990 democratizers using Our World in Data (OWID) panels. The identification strategy employs a combination of fixed effects estimation, instrumental variables (IV), and system GMM to address endogeneity, reverse causality, and omitted variable bias. The primary innovation is adapting the Dippel et al. (2017) framework for mediation analysis in IV settings to a panel data context with moderated mediation. Key recommendations include: (1) Primary estimation using system GMM with interaction terms for moderation combined with three-stage 2SLS for mediation pathways; (2) Identification via country and year fixed effects plus IV with trade partners' income and lagged savings as instruments; (3) Mediation testing using panel bootstrap with 1000+ replications clustering by country; (4) Sensitivity analysis using specification curve with 324 combinations of lags, measures, and fixed effects. The research draws on major methodological papers including Acemoglu et al. (2008) on income and democracy, Bullock & Ha (2011) on mediation analysis challenges, Wawro (2002) on dynamic panel data in political science, and Dippel et al. (2017) on IV mediation frameworks. The output includes detailed model specifications, instrument recommendations with validity tests, step-by-step mediation testing procedures, comprehensive sensitivity analysis plans, and implementation roadmaps for Stata and R.

## Research Findings

## Comprehensive Answer: Identification Strategy for Mediated Moderation Model

### Executive Summary

This research provides a comprehensive identification strategy for estimating a mediated moderation model where welfare state capacity moderates the inequality→educational polarization→democratic resilience pathway in post-1990 democratizers using Our World in Data (OWID) panel data [1][2][3][4][5].

### 1. Primary Identification Strategy

The recommended approach combines **fixed effects (FE)** with **instrumental variables (IV)** and **system GMM** estimation [2][4]. This approach addresses three major identification challenges:

1. **Omitted variable bias**: Country fixed effects control for time-invariant factors (history, culture, geography) that affect both inequality and democracy [2].
2. **Reverse causality**: IV estimation addresses potential endogeneity (democratic resilience may affect inequality) [2][3].
3. **Dynamic persistence**: System GMM handles lagged dependent variables and endogenous regressors in panel data [4].

**Theoretical justification**: Acemoglu et al. (2008) demonstrate that 'controlling for country-specific factors by including country fixed effects removes the statistical association between income per capita and various measures of democracy' [2]. They explicitly warn that 'fixed effects are certainly no substitute for instrumental-variables or structural estimation with valid exclusion restrictions' [2], justifying our combined FE + IV approach.

### 2. Mediated Moderation Framework

Following Dippel et al. (2017) 'Instrumental Variables and Causal Mechanisms' [3], we adapt their three-stage 2SLS framework for panel data:

**Stage 1** (First-stage): 
```
Education_{it} = π₀ + π₁(Z_inequality)_{it} + π₂(Welfare)_{it} + π₃(Controls)_{it} + μ_i + λ_t + ε_{it}
```

**Stage 2** (Reduced form):
```
Democracy_{it} = α₀ + α₁(Z_inequality)_{it} + α₂(Welfare)_{it} + α₃(Controls)_{it} + μ_i + λ_t + ε_{it}
```

**Stage 3** (Second stage):
```
Democracy_{it} = β₀ + β₁(Education̂)_{it} + β₂(Welfare)_{it} + β₃(Controls)_{it} + μ_i + λ_t + ε_{it}
```

**Mediated (indirect) effect**: α₁ × β₁ (product of coefficients from Stage 2 and Stage 3) [3].

**Moderation test**: Add interaction term Inequality × Welfare in Stage 1 equation to test whether welfare state buffers inequality's effect on education.

### 3. Instrument Recommendations

**For inequality**:
1. **Trade-share weighted average income of trading partners** [2]: Predicted income based on trade shares affects country's income but should not directly affect democracy except through income channel. Acemoglu et al. (2008) show this instrument has 'considerable explanatory power for income per capita' [2].
2. **Past savings rates (lagged 5-10 years)** [2]: Affects income per capita but should not directly affect democracy.
3. **Historical settler mortality rates** (for former colonies only) [Acemoglu, Johnson & Robinson 2001]: Affects long-run institutional development including inequality.

**For welfare spending** (more challenging):
1. **Fiscal capacity (tax revenue as % of GDP)**: Affects welfare spending but may be influenced by political factors [Tang & Wang 2020].
2. **Trade openness**: May increase demand for welfare state (Rogowski 1989) but may also directly affect inequality and democracy.

**Instrument validity tests** [2][3]:
- F-test for weak instruments (F > 10 rule of thumb, Stock & Yogo 2005)
- Hansen J-test for overidentifying restrictions (p > 0.05 fails to reject)
- Arellano-Bond test for AR(1) and AR(2) autocorrelation
- Kleinberg-Paap rk LM statistic for underidentification

### 4. Estimation Strategy in Detail

**Fixed effects specification**:
- Country fixed effects (μ_i): Control for all time-invariant country characteristics [2]
- Year fixed effects (λ_t): Control for global time trends (third-wave democratization, global inequality trends) [2]
- Standard errors: Two-way clustering at country level and time level [Cameron & Miller 2015]

**Lag structure**:
- **3-5 year lag** for inequality→democracy relationship based on theoretical persistence of inequality effects (Acemoglu & Robinson 2006) [2]
- Inequality is slow-moving; use 3-year distributed lag or moving average
- Education effects may be faster (1-2 years)
- Test robustness with 1, 3, 5, and 10-year lags

**System GMM specification** [4]:
- Estimator: `xtabond2` in Stata or `pgmm` in R
- Moment conditions: Lagged levels as instruments for differenced equations, lagged differences as instruments for level equations
- Collapse instrument matrix to avoid overfitting (Roodman 2009)
- Hansen test for overidentifying restrictions
- Arellano-Bond test for AR(1) and AR(2)

### 5. Mediation Testing Approach

**Bootstrap procedure for panel data** [5]:
- **Nonparametric bootstrap**: 1000+ replications with panel structure preserved
- **Cluster bootstrap**: Cluster by country and use `idcluster()` option to maintain panel structure [5]
- **Stata implementation**: 
  ```stata
  xtreg democracy education welfare, fe vce(bootstrap, rep(1000) seed(123))
  ```
  Or use `bootstrap` command with `cluster()` and `idcluster()` options [5].

**Confidence intervals**:
- Bias-corrected and accelerated (BCa) bootstrap CI
- Alternative: Monte Carlo confidence intervals (Preacher & Selig 2012)

**Power considerations**:
- Bootstrap requires large N for valid inference
- With ~80 countries and T=30, power may be limited
- Consider wild bootstrap or parametric bootstrap alternatives

### 6. Sensitivity Analysis Plan

**Specification curve analysis** (Simonsohn et al. 2020):
- **Dimensions**: Lag structure (4), democracy measure (3), inequality measure (3), fixed effects (3), SE clustering (3)
- **Total specifications**: 4 × 3 × 3 × 3 × 3 = 324 models
- **Reporting**: Median coefficient, interquartile range, fraction of specifications with p<0.05

**Additional robustness checks**:
1. Subsample analysis by region (Europe/Central Asia, Latin America, East Asia/Pacific, Sub-Saharan Africa)
2. Subsample by initial democracy level (low/medium/high at 1990)
3. Placebo tests with false mediators (geography, climate variables)
4. Alternative welfare state measures (social spending % GDP, welfare state generosity index, V-Dem social welfare index)
5. Test for weak instruments and report Kleinberg-Paap rk LM statistic

**Success criteria for robustness**:
1. Coefficient on inequality→democracy pathway remains significant (p<0.05) in >75% of specifications
2. Indirect effect through education remains significant in >70% of specifications
3. Moderation effect (interaction term) remains significant in >60% of specifications
4. Coefficient signs remain consistent across specifications (no sign flipping)
5. Instrument F-statistics >10 in all IV specifications

### 7. Data Requirements and Sample Selection

**OWID variables needed**:
1. **Democracy**: V-Dem Electoral Democracy Index, Polity IV score, Freedom House
2. **Inequality**: Gini coefficient, top 10% income share, Palma ratio
3. **Education**: Educational equality index (V-Dem), school enrollment rates, educational attainment
4. **Welfare state**: Social spending (% GDP), tax revenue (% GDP), V-Dem welfare index
5. **Controls**: GDP per capita, trade openness, population, ethnic fractionalization, resource rents

**Sample selection**: Post-1990 democratizers
- Definition: Countries with Polity IV score <0 (autocracy) in 1990 that transitioned to democracy (Polity score >5) by 1995-2000
- Alternative: Use V-Dem or Freedom House to define democratization episodes
- Include only countries with population >500,000 and available data for key variables

### 8. Implementation Roadmap

**Software recommendations**:
- **PRIMARY**: Stata 17+ with `xtabond2`, `ivreg2`, `bootstrap` commands. Stata is standard in political science; excellent panel data capabilities.
- **ALTERNATIVE**: R with `plm`, `lme4`, `mediation`, `ivpack` packages. Better for bootstrap and simulation.
- **AVOID**: Python for this analysis - limited panel data IV capabilities compared to Stata/R.

**Computing requirements**:
- **Memory**: 8GB+ RAM for bootstrap with 1000+ replications on panel with N=80, T=30
- **Processing time**: ~2-4 hours for full specification curve with 324 models on standard laptop
- **HPC**: Consider using high-performance computing cluster for bootstrap with 10,000+ replications

### 9. Potential Pitfalls and Contingency Plans

**Pitfall 1: Weak instruments**
- **Problem**: Instrument F-statistic < 10 (weak identification)
- **Solution**: Report Fuller(4) or LIML estimates; use more restrictive model; find additional instruments; report confidence intervals robust to weak instruments (Anderson-Rubin confidence region)

**Pitfall 2: Small T (time periods) problem**
- **Problem**: T = 30 years may be insufficient for system GMM
- **Solution**: Collapse to 5-year periods (T = 6); use difference GMM instead of system GMM; use fixed effects with IV

**Pitfall 3: Mediation testing power**
- **Problem**: Bootstrap requires large N for valid inference. With ~80 countries, power may be limited.
- **Solution**: Use wild bootstrap; use parametric bootstrap; consider Bayesian approach with informative priors

**Pitfall 4: Data quality and missing values**
- **Problem**: OWID aggregates from multiple sources; data quality flags vary. Missing data may not be MCAR.
- **Solution**: Check OWID data quality flags; use multiple imputation (MICE); conduct sensitivity analysis with listwise deletion vs. imputation

### 10. Limitations and Alternative Views

**Identification assumptions** (untestable):
1. **Exclusion restriction for IV**: Instruments must affect outcome ONLY through endogenous regressor. This requires strong theoretical justification.
2. **No unobserved confounding in mediation**: Even with IV, unobserved variables may affect both mediator and outcome (Bullock & Ha 2011) [1].
3. **Monotonicity for LATE interpretation**: IV estimates local average treatment effect for compliers.

**Alternative views in literature**:
1. Some argue inequality has no effect on democracy (Acemoglu et al. 2008) [2]
2. Others find education has diminishing returns for democracy (adult education may not affect political behavior)
3. Welfare state may be endogenous to democracy (reverse causality concern)
4. Panel data mediation may be better approached with SEM rather than sequential 2SLS (Imai et al. 2010)

**Robustness concerns**:
1. OWID data quality: Aggregated from multiple sources with different methodologies
2. Small sample bias in IV: N=80 countries may be insufficient for reliable IV estimation
3. Dynamic panel bias: Nickell bias in fixed effects models with lagged DV and small T
4. Model uncertainty: Mediated moderation is complex; simpler models may be more transparent

### Conclusion

This research provides a rigorous identification strategy for estimating a mediated moderation model in panel data, drawing on state-of-the-art methodological approaches from political science and econometrics [1][2][3][4][5]. The strategy addresses major identification challenges through a combination of fixed effects, instrumental variables, and system GMM estimation. The innovation of adapting the Dippel et al. (2017) IV mediation framework [3] to panel data with moderated mediation provides a novel methodological contribution. However, the approach requires strong assumptions (exclusion restriction, no unobserved confounding) that must be justified theoretically and tested through sensitivity analysis. The comprehensive sensitivity analysis plan with 324 specifications provides a roadmap for assessing robustness. Implementation in Stata or R is feasible with available commands and packages. The expected contribution is a methodologically rigorous analysis of the inequality-democracy relationship that meets the highest standards of political methodology for publication in APSR, World Politics, or Journal of Democracy.

## Sources

[1] [Mediation Analysis Is Harder than It Looks (Cambridge Handbook of Experimental Political Science)](https://johnbullock.org/papers/mediation_harder_final.pdf) — Warns about endogeneity bias in mediation analysis with nonexperimental data; recommends experimental or IV approaches. Demonstrates that standard Baron-Kenny method is biased when mediator is not randomized.

[2] [Income and Democracy (American Economic Review 2008)](https://economics.mit.edu/sites/default/files/publications/income%20and%20democracy.pdf) — Uses country fixed effects and IV estimation with trade partners' income as instrument; finds no causal effect of income on democracy once fixed effects included. Provides justification for FE + IV approach.

[3] [Instrumental Variables and Causal Mechanisms: Unpacking the Effect of Trade on Workers and Voters (NBER 2017)](https://www.nber.org/system/files/working_papers/w23209/revisions/w23209.rev2.pdf) — Proposes framework for mediation analysis in IV settings using three 2SLS estimations; directly applicable to our mediated moderation model. Under linearity, mediation effects can be evaluated using three separate 2SLS regressions.

[4] [Estimating Dynamic Panel Data Models in Political Science (Political Analysis 2002)](http://www-personal.umich.edu/~franzese/Wawro.EstDynamicPanelsPolSci.PA2002.pdf) — Reviews GMM estimators for dynamic panels; discusses system GMM for models with lagged dependent variables and endogenous regressors. Provides guide to implementing GMM in political science applications.

[5] [How do I obtain bootstrapped standard errors with panel data? (Stata FAQ)](https://www.stata.com/support/faqs/statistics/bootstrap-with-panel-data/) — Explains how to implement bootstrap with panel data in Stata, clustering by panel ID. Must specify cluster() and idcluster() options to maintain panel structure in bootstrap samples.

## Follow-up Questions

- What are the most valid instruments for welfare state capacity in post-1990 democratizers, given the difficulty of finding instruments that satisfy the exclusion restriction?
- How should we handle the trade-off between model complexity (mediated moderation) and transparency/parsimony for publication in top political science journals?
- What is the optimal way to test for and report sensitivity to the exclusion restriction assumption in IV mediation models, given that this assumption is fundamentally untestable?

---
*Generated by AI Inventor Pipeline*
