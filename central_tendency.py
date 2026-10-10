import numpy as np
import pandas as pd


spending = np.array([100, 150, 200, 250, 2300])

print("Mean:", np.mean(spending))
print("Median:", np.median(spending))
print("Mode:", pd.Series(spending).mode().tolist())
