from scipy.stats import beta


alpha = 21
beta_param = 81

dist = beta(alpha, beta_param)

print("Posterior mean:", dist.mean())
print("P(p <= 0.25):", dist.cdf(0.25))
print("95% credible interval:", dist.ppf([0.025, 0.975]))
