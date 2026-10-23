from scipy.stats import norm

mean = 500
se = 10

# 95% Normal-based confidence interval
z = norm.ppf(0.975)

lower = mean - z * se
upper = mean + z * se

print("95% CI:", round(lower, 2), round(upper, 2))
