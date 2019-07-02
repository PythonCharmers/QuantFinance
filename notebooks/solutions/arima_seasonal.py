#1. In the above example we have specified a seasonal ARMIMA model of 0, 1, 0 (P,Q,Q) with a period of 4, since 
#    we are using quarterly data.

#2.

wheat_price = quandl.get("ODA/PWHEAMT_USD", collapse="monthly")
seasonal_model_wheat = SARIMAX(changes, order=(1, 1, 1), seasonal_order=(0, 1, 0, 12))
result_wheat = seasonal_model_wheat.fit()
result_wheat.summary()
