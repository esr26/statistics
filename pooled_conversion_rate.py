control_conversions = 100
control_users = 1000

treatment_conversions = 130
treatment_users = 1000

pooled_p = (
    control_conversions + treatment_conversions
) / (
    control_users + treatment_users
)

print(f"Pooled conversion rate: {pooled_p:.1%}")
