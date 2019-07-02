
# Question 1
euro_result = adfuller(euro_fit.fittedvalues)
print('ADF Statistic: {:.2f}'.format(euro_result[0]))
print('p-value: {:.2f}'.format(euro_result[1]))

usd_result = adfuller(usd_fit.fittedvalues)
print('ADF Statistic: {:.2f}'.format(usd_result[0]))
print('p-value: {:.2f}'.format(usd_result[1]))


# Question 2
euro_diff = euros.diff()
result = adfuller(euros_diff[~np.isnan(euros_diff)])

usd_diff = usd.diff()
result = adfuller(usd_diff[~np.isnan(usd_diff)])

# Question 3 

euro_log = np.log(euros)
usd_log = np.log(usd)
