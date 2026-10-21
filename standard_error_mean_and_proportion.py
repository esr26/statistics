import numpy as np

# Mean: Average customer spending
sample_sd = 200
n_mean = 400

se_mean = sample_sd / np.sqrt(n_mean)

# Proportion: Customer conversion rate
conversions = 200
n_prop = 1000

p_hat = conversions / n_prop

se_prop = np.sqrt(
    p_hat * (1 - p_hat) / n_prop
)

print("Mean SE:", round(se_mean, 2))
print("Conversion rate:", round(p_hat, 4))
print("Proportion SE:", round(se_prop, 5))
