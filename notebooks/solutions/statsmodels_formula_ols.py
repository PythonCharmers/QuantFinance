
split_point = int(2 * len(X) / 3)
data_train, data_test = data[:split_point], data[split_point:]


import statsmodels.formula.api as smf
est = smf.ols(formula='Inflation ~ InterestRate + AUDUSD', data=data_train).fit()  # Adds the constant for us

y_pred = est.predict(data_test)
y_pred.name = "PredictedInflation"
pd.concat([data_test["Inflation"], y_pred], axis=1).plot()