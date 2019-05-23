# Use KPSS to test for stationarity.
from statsmodels.tsa.stattools import kpss

kpss_stat, p_value, lags, crit = kpss(xrp)
print("XRP p_value:", p_value)

kpss_stat, p_value, lags, crit = kpss(eth)
print("ETH p_value:", p_value)


from statsmodels.tsa.arima_model import ARIMA as arima

xrp_model_arima = arima(xrp, order=(4,1, 2))  #Remember if we use d=0 we're back to using the ARMA model!
eth_model_arima = sms.tsa.ARMA(eth, order=(3, 1, 2))

xrp_results_arima = xrp_model_arima.fit()
eth_results_arima = eth_model_arima.fit()

xrp_results_arima.summary()
eth_results_arima.summary()
