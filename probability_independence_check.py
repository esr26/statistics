# Check independence from observed probabilities

p_prime = 300 / 1000
p_purchase = 250 / 1000
p_both = 150 / 1000

expected_if_independent = p_prime * p_purchase

print("Observed P(Both):", p_both)
print("Expected if independent:", expected_if_independent)
