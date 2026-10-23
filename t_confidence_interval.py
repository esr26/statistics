import numpy as np
from scipy.stats import t

watch_times = np.array([100, 120, 130, 115, 140, 125])

mean = watch_times.mean()
sd = watch_times.std(ddof=1)
se = sd / np.sqrt(len(watch_times))

ci = t.interval(
    confidence=0.95,
    df=len(watch_times)-1,
    loc=mean,
    scale=se
)

print("95% t CI:", ci)
