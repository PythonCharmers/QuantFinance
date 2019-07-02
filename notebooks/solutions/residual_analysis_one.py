#1
from statsmodels.tsa.stattools import bds

X = x
X = sm.add_constant(x)
model = sm.OLS(y_quad, X)
results = model.fit()
y_pred = results.predict(X)

errors = y_pred - y_quad
plt.plot(x, errors, 'ro')

stat, p = bds(x)
stat, p


#2
from statsmodels.stats.diagnostic import acorr_ljungbox

lb, p = acorr_ljungbox(errors)
lb, p


