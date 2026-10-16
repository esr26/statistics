import numpy as np


rng = np.random.default_rng(42)

population_mean = 500
population_sd = 200
sample_size = 100
num_samples = 10_000

# Repeated independent samples of size 100
samples = rng.normal(
    loc=population_mean,
    scale=population_sd,
    size=(num_samples, sample_size),
)

sample_means = samples.mean(axis=1)

print("Mean of sample means:", sample_means.mean())
print("SD of sample means:", sample_means.std())
print("Theoretical SE:", population_sd / np.sqrt(sample_size))
