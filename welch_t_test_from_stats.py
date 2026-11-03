from scipy.stats import ttest_ind_from_stats

# Netflix control
mean_c = 100
std_c = 20
n_c = 25

# Netflix treatment
mean_t = 110
std_t = 25
n_t = 25

t_stat, p_value = ttest_ind_from_stats(
    mean1=mean_t,
    std1=std_t,
    nobs1=n_t,
    mean2=mean_c,
    std2=std_c,
    nobs2=n_c,
    equal_var=False
)

print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.3f}")
