
# Question 1
euro_result = adfuller(euro_fit.fittedvalues)
print('ADF Statistic: {:.2f}'.format(euro_result[0]))
print('p-value: {:.2f}'.format(euro_result[1]))

usd_result = adfuller(usd_fit.fittedvalues)
print('ADF Statistic: {:.2f}'.format(usd_result[0]))
print('p-value: {:.2f}'.format(usd_result[1]))


# Question 2
euro_diff = euros.diff()
usd_diff = usd.diff()


# Question 3 

euro_log = np.log(euros)
usd_log = np.log(usd)