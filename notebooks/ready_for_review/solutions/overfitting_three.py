#1
from sklearn.linear_model import Ridge
# Create a dataset

x = (np.random.random(20) * 10)
y = 3 * x + (np.random.rand(20) * 25)
plt.plot(x, y, 'ro', label="Data")

x = x.reshape(-1,1)
l_model = LinearRegression()
r_model = Ridge(alpha=100)
l_model.fit(x,y)
r_model.fit(x,y)
l_pred = l_model.predict(x)
r_pred = r_model.predict(x)
plt.plot(l_pred, label="Linear")
plt.plot(r_pred, label="Ridge")


#2
from sklearn.model_selection import GridSearchCV

test_range = np.arange(100)
param_grid = {"alpha": test_range}
gs = GridSearchCV(Ridge(),param_grid)
gs.fit(x, y)
gs.best_params_
