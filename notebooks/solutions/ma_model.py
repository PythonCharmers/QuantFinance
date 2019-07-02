# Exercise solution
import my_secrets
quandl.ApiConfig.api_key = my_secrets.QUANDL_API_KEY

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'], 
                        qopts = { 'columns': ['adj_close'] }, 
                        date = { 'gte': '2017-01-01', 'lte': '2019-01-01' }, 
                        paginate=True)

changes = data['adj_close'].diff().dropna()
model = sm.tsa.ARMA(changes, order=(0,1))
stock_results= model.fit()

stock_results.summary()

# Extended exercise solution
epsilons = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 0]) # Try different combinations here.

theta = -2
print("theta: ", theta)

X = epsilons[1:] + theta * epsilons[:-1]
print(np.mean(epsilons))

plt.plot(X)
