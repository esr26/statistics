from scipy.stats import uniform


# Uniform distribution from 0 to 10
a = 0
b = 10

# Note: SciPy uses loc and scale
dist = uniform(loc=a, scale=b - a)

print("PDF at 6:", dist.pdf(6))
print("CDF at 6:", dist.cdf(6))

# Probability between 4 and 7
print("P(4 < X < 7):", dist.cdf(7) - dist.cdf(4))

print("Mean:", dist.mean())
print("Variance:", dist.var())
