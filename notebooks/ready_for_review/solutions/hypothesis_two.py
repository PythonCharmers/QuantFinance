#1 
import quandl
xrate = quandl.get("RBA/FXRUSD-AUD-USD-Exchange-Rate")

#2
xdelta = xrate.diff().dropna()
up = xdelta[xdelta["Value"] > 0]
down = xdelta[xdelta["Value"] < 0]
up_result = len(up)/len(xdelta)
down_result = len(down)/len(xdelta)
up_result

#Extended Exercise

iters = range(1000) #Repeat our experiment 1000 times.
results = []

for i in iters:
    data = np.random.normal(size=365) #Generate normally distributed data for 1 year.
    data = np.array([x > 0 for x in data]) # Up = True, Down = False

    test_result = data.sum()/len(data) #'True' is stored as a 1, so we can use sum to count.
    results.append(test_result)

plt.hist(results)

stats.ttest_1samp(results, 0.5)
print('t stat: {:.4f}, p value: {:4f}'.format(t_stat, p_val))



