from scipy import stats

n = int(len(X) / 2)

stats.levene(X[:n], X[n:])

# Extended exercise solution
import statsmodels.api as sm

# Create some random 
y = np.random.random(len(X))
est = sm.OLS(y, X).fit()

y_pred = est.fittedvalues

residuals = y_pred - y

plt.plot(y_pred, residuals, 'ro')  # No clear pattern == white noise
