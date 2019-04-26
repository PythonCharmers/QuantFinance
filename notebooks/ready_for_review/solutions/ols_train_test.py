split_point = int(2 * len(X) / 3)
X_train, X_test = X[:split_point], X[split_point:]
y_train, y_test = y[:split_point], y[split_point:]


# Fit an OLS model and get a summary
est = sm.OLS(y_train, X_train).fit()

y_pred = est.predict(X_test)
y_pred.name = "PredictedInflation"

pd.concat([y_test, y_pred], axis=1).plot()  # Not as good...