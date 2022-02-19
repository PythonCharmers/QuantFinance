
# Solutions
from statsmodels.tsa.stattools import kpss

kpss_stat, p_value, lags, crit = kpss(train_residuals)

print("reject H0:",p_value < 0.05)

kpss_stat, p_value, lags, crit = kpss(test_residuals)

print("reject H0:",p_value < 0.05)
