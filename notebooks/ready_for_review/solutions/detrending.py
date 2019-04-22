from scipy.signal import detrend

prices['gold_detrended'] = detrend(prices['gold'])
prices['wheat_detrended'] = detrend(prices['wheat'])
prices[['gold_detrended', 'wheat_detrended']].plot()

prices[['gold_detrended', 'wheat_detrended']].corr()