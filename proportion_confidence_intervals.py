from statsmodels.stats.proportion import proportion_confint

conversions = 200
users = 1000

# 95% Wald interval
wald_ci = proportion_confint(
    count=conversions,
    nobs=users,
    alpha=0.05,
    method="normal"
)

# 95% Wilson interval
wilson_ci = proportion_confint(
    count=conversions,
    nobs=users,
    alpha=0.05,
    method="wilson"
)

print("Wald CI:", wald_ci)
print("Wilson CI:", wilson_ci)

# Small-sample example
print(
    "Wilson (1/20):",
    proportion_confint(
        count=1,
        nobs=20,
        alpha=0.05,
        method="wilson"
    )
)
