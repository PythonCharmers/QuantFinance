
from statsmodels.tsa.tsatools import detrend

Xst_detrended = detrend(X_stationary)
Xnonst_detrended = detrend(X_non_stationary)
Xar1_detrended = detrend(X_AR1)


from statsmodels.tsa.stattools import adfuller

# X_stationary
plt.plot(X_stationary, alpha=0.5)
plt.plot(Xst_detrended, 'r--', alpha=0.5)  # No difference

adf, p_value, *_ = adfuller(Xst_detrended)

p_value < 0.05, p_value  # Reject hypothesis of a unit root, which indicates stationary

plt.plot(X_non_stationary, alpha=0.5)
plt.plot(Xnonst_detrended)  # Removed linear increase

adf, p_value, *_ = adfuller(Xnonst_detrended)

p_value < 0.05, p_value  # Reject hypothesis of a unit root, which indicates stationary

plt.plot(X_AR1, alpha=0.5)
plt.plot(Xar1_detrended)  # linear detrends aren't perfect

adf, p_value, *_ = adfuller(Xar1_detrended)

p_value < 0.05, p_value  # Do NOT hypothesis of a unit root, which indicates stationary

# In this case, linear detrend is not sufficient to make stationary
