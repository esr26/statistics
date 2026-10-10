import numpy as np


loading_times = np.array([1, 2, 2, 3, 3, 4, 5, 6, 8, 20])

print("Mean:", np.mean(loading_times))
print("P50:", np.percentile(loading_times, 50))
print("P90:", np.percentile(loading_times, 90))
print("P95:", np.percentile(loading_times, 95))

# IQR-based outlier screening
q1, q3 = np.percentile(loading_times, [25, 75])
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = loading_times[
    (loading_times < lower) | (loading_times > upper)
]

print("Potential outliers:", outliers)
