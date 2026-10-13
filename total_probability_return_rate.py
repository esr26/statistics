p_prime = 0.60
p_non_prime = 0.40

return_prime = 0.10
return_non_prime = 0.20

overall_return_rate = (
    p_prime * return_prime
    + p_non_prime * return_non_prime
)

print(f"Overall return rate: {overall_return_rate:.2%}")
