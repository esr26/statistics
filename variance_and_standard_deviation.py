import numpy as np


a = np.array([28, 29, 30, 31, 32])
b = np.array([10, 20, 30, 40, 50])

print("Service A")
print("Mean:", np.mean(a))
print("Variance:", np.var(a))
print("Std Dev:", np.std(a))

print("\nService B")
print("Mean:", np.mean(b))
print("Variance:", np.var(b))
print("Std Dev:", np.std(b))
