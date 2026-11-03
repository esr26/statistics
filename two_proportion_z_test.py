from statsmodels.stats.proportion import proportions_ztest

# Number of purchases
conversions = [100, 130]

# Total users
sample_sizes = [1000, 1000]

# Two-sided hypothesis test
z_stat, p_value = proportions_ztest(
    count=conversions,
    nobs=sample_sizes,
    alternative="two-sided"
)

print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
