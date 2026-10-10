import pandas as pd


df = pd.DataFrame({
    "sessions": [1, 2, 3, 4],
    "engagement": [1, 4, 9, 16]
})

pearson = df["sessions"].corr(
    df["engagement"], method="pearson"
)

spearman = df["sessions"].corr(
    df["engagement"], method="spearman"
)

print("Pearson:", round(pearson, 3))
print("Spearman:", round(spearman, 3))
