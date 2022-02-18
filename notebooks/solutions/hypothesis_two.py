#1 
import quandl
xrate = quandl.get("RBA/FXRUSD-AUD-USD-Exchange-Rate")

#2
xdelta = xrate.diff().dropna()
xdelta['lag'] = xdelta['Value'].shift(1)
xdelta = xdelta.dropna()
xdelta['matched_movement'] = xdelta['Value']*xdelta['lag'] > 0 # compare values to lagged values
samp_prop = np.sum(xdelta['matched_movement'])/xdelta.shape[0] # get proportion of movements that match the previous movement
samp_prop


#Extended Exercise

iters = range(1000) #Repeat our experiment 1000 times.
results = []
distribution = stats.norm(0, 1)

for i in iters:
    X = distribution.rvs(365) # create randomly distributed data for a year
    data = pd.DataFrame([X[i] for i in range(len(X))])
    data.columns = ['Value']
    data['lag'] = data['Value'].shift(1)
    data = data.dropna()
    data['matched_movement'] = data['Value']*data['lag'] > 0 # compare values to lagged values
    data_prop = np.sum(data['matched_movement'])/data.shape[0]
    results.append(data_prop)

plt.hist(results)

t_stat, p_val = stats.ttest_1samp(results, 0.5)
print('t stat: {:.4f}, p value: {:4f}'.format(t_stat, p_val))



