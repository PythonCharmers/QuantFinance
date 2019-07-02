%run setup.ipy

import quandl
import my_secrets
quandl.ApiConfig.api_key = my_secrets.QUANDL_API_KEY

xrp = quandl.get("BITFINEX/XRPUSD")["Last"]
eth = quandl.get("BITFINEX/ETHUSD")["Last"]

# Should we replace the index? Some dates are missing so we can't set a frquency to 'D' without actually
# replacing the entire index? This generates a lot of warnings...


# When we've played with values a bit, we can then use the below.
from statsmodels.tsa import stattools
xrp_stats = stattools.arma_order_select_ic(xrp) 
eth_stats = stattools.arma_order_select_ic(eth) 
print("XRP: ", xrp_stats)
print("ETH:", eth_stats)

from statsmodels import api as sms
xrp_model = sms.tsa.ARMA(xrp, order=(4, 2))
eth_model = sms.tsa.ARMA(eth, order=(3, 2))

xrp_results = xrp_model.fit()
eth_results = eth_model.fit()

xrp_results.summary()
eth_results.summary()
