from statsmodels.tsa.seasonal import seasonal_decompose

X = sm.add_constant(x)
model = sm.OLS(y_seasonal, X)
results = model.fit()
y_pred = results.predict(X)

errors = y_pred - y_seasonal
plt.plot(x, errors, 'ro')

# Apply seasonal decomposition to our data
result = seasonal_decompose(y_seasonal, model="additive", freq=12)
# Plot the residuals after decomposition
plt.plot(x, result.resid, 'ro')

#Remove the seasonal trending from our data
y_clean = y_seasonal - result.seasonal

model = sm.OLS(y_clean, X)
results = model.fit()
y_pred = results.predict(X)

errors = y_pred - y_clean
#Plot our cleaned Data
plt.plot(x, y_clean)
# Check residuals
plt.plot(x, errors, 'ro')
