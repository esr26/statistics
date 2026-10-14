from scipy.stats import norm


mu = 10
sigma = 2

# Density at 10 seconds
print("PDF:", norm.pdf(10, loc=mu, scale=sigma))

# Probability loading time <= 10
print("CDF:", norm.cdf(10, loc=mu, scale=sigma))

# Probability 8 < X < 12
p_between = (
    norm.cdf(12, loc=mu, scale=sigma)
    - norm.cdf(8, loc=mu, scale=sigma)
)
print("Between 8 and 12:", p_between)

# Probability loading time > 14
print("Above 14:", norm.sf(14, loc=mu, scale=sigma))

# 95th percentile
print("P95:", norm.ppf(0.95, loc=mu, scale=sigma))
