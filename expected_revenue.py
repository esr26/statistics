import numpy as np


# Possible spending amounts
revenue = np.array([0, 500, 2000])

# Probability of each outcome
probabilities = np.array([0.60, 0.30, 0.10])

expected_revenue = np.sum(revenue * probabilities)

print("Expected revenue:", expected_revenue)

# Expected revenue from 10,000 visitors
expected_total = expected_revenue * 10_000

print("Expected total:", expected_total)
