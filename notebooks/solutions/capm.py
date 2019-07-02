import quandl

import my_secrets
quandl.ApiConfig.api_key = my_secrets.QUANDL_API_KEY

sp500 = quandl.get("CHRIS/CME_SP1")

sp500_sample = sp500.loc["2016":"2018"].dropna()

market = sp500_sample['Last'].pct_change().dropna() * 100

cola = quandl.get("WIKI/KO")

cola_sample = cola['2016':"2018"]

coca = cola_sample['Close'].pct_change().dropna() * 100

market_variance = market["2016":"2018"].var()
print(f"Market Variance: {market_variance}")

stock_cov = market.corr(coca)

print(f"Stock Covariance: {stock_cov}")

beta = stock_cov / market_variance

print(f"Beta: {beta}")

e = ending_balance = sp500_sample.iloc[-1]["Last"]
s = starting_balance = sp500_sample.iloc[0]["Last"]
n = number_years = 3  # 2016, 2017, 2018
return_on_market = (e / s) ** (1 / n) - 1

print(f"Return on Market: {return_on_market}")

capm = .025  + beta * (return_on_market - .025)
print(f"CAPM: {capm}")
