from scipy.stats import geom


p = 0.2

print("P(first click on 3rd):", geom.pmf(3, p))
print("P(first click by 3rd):", geom.cdf(3, p))
print("Expected trials:", geom.mean(p))
print("Variance:", geom.var(p))
