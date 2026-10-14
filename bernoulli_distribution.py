import numpy as np
from scipy.stats import bernoulli


p = 0.30

# Probability of each outcome
print("P(Purchase):", bernoulli.pmf(1, p))
print("P(No Purchase):", bernoulli.pmf(0, p))

# Theoretical mean and variance
print("Mean:", bernoulli.mean(p))
print("Variance:", bernoulli.var(p))

# Simulate 10,000 customer visits
rng = np.random.default_rng(42)
visits = rng.binomial(1, p, size=10_000)

print("Observed conversion:", visits.mean())
