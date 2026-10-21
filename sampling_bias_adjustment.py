import numpy as np

satisfaction = np.array([0.90, 0.60])

sample_weights = np.array([0.80, 0.20])
population_weights = np.array([0.20, 0.80])

naive_estimate = np.dot(
    sample_weights, satisfaction
)

adjusted_estimate = np.dot(
    population_weights, satisfaction
)

print("Naive estimate:", naive_estimate)
print("Adjusted estimate:", adjusted_estimate)
