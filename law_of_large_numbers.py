import numpy as np


rng = np.random.default_rng(42)

# True conversion probability
p = 0.20

# Simulate 10,000 independent customers
conversions = rng.binomial(1, p, size=10_000)

# Running average
running_conversion = (
    np.cumsum(conversions)
    / np.arange(1, len(conversions) + 1)
)

for n in [10, 100, 1000, 10000]:
    print(n, round(running_conversion[n - 1], 4))
