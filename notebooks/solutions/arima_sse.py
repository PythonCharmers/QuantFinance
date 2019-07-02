from datetime import datetime

start_date = datetime(2015, 1, 1)
end_date = datetime(2029, 10, 1)

train = changes.loc[:start_date]
test = changes.loc[start_date:end_date]

model = ARIMA(train, order=(1, 0, 2))
results = model.fit()
results.summary()

y_pred = results.predict(start_date, end_date)
y_pred.name = "Predictions"
y_pred.plot(title="Predictions")
test.plot(title="Actual")

test_s = test["Value"] #Convert to a series to match our predicted data
sse = np.sum((y_pred - test_s)**2)

sse
