import numpy as np
import pandas as pd


data = [2, 4, 6]

# Population variance
print(np.var(data, ddof=0))

# Sample variance
print(np.var(data, ddof=1))

# pandas uses sample variance by default
print(pd.Series(data).var())
