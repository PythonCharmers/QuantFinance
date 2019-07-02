
# Solutions
from statsmodels.tsa.stattools import kpss

kpss_stat, p_value, lags, crit = kpss(X_stationary)

p_value > 0.05, p_value   # Accept hypothesis of stationarity

kpss_stat, p_value, lags, crit = kpss(X_non_stationary)

p_value > 0.05, p_value  # Reject hypothesis of stationarity

kpss_stat, p_value, lags, crit = kpss(X_AR1)

p_value > 0.05, p_value  # Reject hypothesis of stationarity

from statsmodels.tsa.stattools import adfuller

adf, p_value, *_ = adfuller(X_stationary)

p_value < 0.05, p_value  # Reject hypothesis of a unit root, which indicates stationary
