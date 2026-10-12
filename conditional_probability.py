total_users = 1000
reels_users = 400
purchasers = 200
both = 120

p_purchase_given_reels = both / reels_users
p_reels_given_purchase = both / purchasers

print("P(Purchase | Reels):", p_purchase_given_reels)
print("P(Reels | Purchase):", p_reels_given_purchase)
