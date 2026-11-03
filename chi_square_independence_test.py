import numpy as np
from scipy.stats import chi2_contingency

# Rows: Mobile, TV
# Columns: Cancelled, Not cancelled
observed = np.array([
    [30, 70],
    [10, 90]
])

chi2, p_value, dof, expected = chi2_contingency(
    observed,
    correction=False
)

print(f"Chi-square: {chi2:.2f}")
print(f"Degrees of freedom: {dof}")
print(f"P-value: {p_value:.4f}")
print("Expected counts:")
print(expected)
