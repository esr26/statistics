from scipy.stats import expon


rate = 3  # requests per minute

# SciPy scale = mean waiting time = 1/rate
dist = expon(scale=1 / rate)

print("PDF at 20 sec:", dist.pdf(1 / 3))
print("P(wait <= 20 sec):", dist.cdf(1 / 3))
print("P(wait > 20 sec):", dist.sf(1 / 3))
print("Mean waiting time (min):", dist.mean())
