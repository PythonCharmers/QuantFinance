from statsmodels.tsa.holtwinters import ExponentialSmoothing

ExponentialSmoothing?

euro = quandl.get("BUNDESBANK/BBEX3_M_AUD_EUR_CM_AC_A01")  # Euros in AUD

euros = euro['Value']
euros.name = "EURO"
euros.head()

usd = quandl.get("BUNDESBANK/BBEX3_M_AUD_USD_CM_AC_A01")['Value']
usd.name = "USD"
usd.head()

ExponentialSmoothing?

euro_model = ExponentialSmoothing(euros)
euro_fit = euro_model.fit()
plt.plot(ts.acf(euro_fit.fittedvalues, nlags=100))

usd_model = ExponentialSmoothing(usd)
usd_fit = usd_model.fit()
plt.plot(ts.acf(usd_fit.fittedvalues, nlags=100))

print("Note that in both cases, you'll generally want to fit the differences or variances, rather than the raw prices")