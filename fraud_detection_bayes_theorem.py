p_fraud = 0.01
recall = 0.90
false_positive_rate = 0.05

p_flag = (
    recall * p_fraud
    + false_positive_rate * (1 - p_fraud)
)

precision = recall * p_fraud / p_flag

print("P(Flag):", round(p_flag, 4))
print("P(Fraud | Flag):", round(precision, 4))
