from scipy.stats import poisson


lam = 3

# Exactly 5 events
print("P(X=5):", poisson.pmf(5, mu=lam))

# At most 2 events
print("P(X<=2):", poisson.cdf(2, mu=lam))

# At least 5 events
print("P(X>=5):", poisson.sf(4, mu=lam))

# Mean and variance
print("Mean:", poisson.mean(mu=lam))
print("Variance:", poisson.var(mu=lam))
