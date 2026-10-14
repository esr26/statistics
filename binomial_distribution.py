from scipy.stats import binom


n = 5
p = 0.2

# Exactly 2 purchases
print("Exactly 2:", binom.pmf(2, n, p))

# At most 2 purchases
print("At most 2:", binom.cdf(2, n, p))

# At least 2 purchases
print("At least 2:", binom.sf(1, n, p))

# At least 1 purchase
print("At least 1:", binom.sf(0, n, p))

# Mean and variance
print("Mean:", binom.mean(n, p))
print("Variance:", binom.var(n, p))
