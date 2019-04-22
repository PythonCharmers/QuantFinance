
from statsmodels.stats import stattools

# In a notebook cell, run:
stattools.jarque_bera?

jbstat, pvalue, skew, kurtosis = stattools.jarque_bera(heights)
print(pvalue)

if pvalue < 0.05:
    print("We reject the null hypothesis that the data is normal")
else:
    print("We cannot reject that the data came from a normal distribution")