total = 100
purchased = 40
coupon = 30
both = 15

p_a = purchased / total
p_b = coupon / total
p_both = both / total

p_or = p_a + p_b - p_both
p_neither = 1 - p_or

print("P(Purchase):", p_a)
print("P(Both):", p_both)
print("P(Either):", p_or)
print("P(Neither):", p_neither)