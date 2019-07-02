#1
train_err = y_pred_low[0:50] - y_low
train_SSE = np.sum(train_err **2)
train_SSE

test_err = y_pred_low[50:100] - y_high
test_SSE = np.sum(test_err **2)
test_SSE

#2

# Fit model to each
params_low = np.polyfit(x_low, y_low, 2)
params_high = np.polyfit(x_high, y_high, 2)

plt.plot(x, y, 'r-')  # Actual data in red

y_pred_low = np.poly1d(params_low)(x)
plt.plot(x, y_pred_low, 'g--')  # Predictions from "low" model in green

y_pred_high = np.poly1d(params_high)(x)
plt.plot(x, y_pred_high, 'k--')  # Predictions from "high" model in black

# Rerun our SSE calculations

train_err = y_pred_low[0:50] - y_low
train_SSE = np.sum(train_err **2)
train_SSE

test_err = y_pred_low[50:100] - y_high
test_SSE = np.sum(test_err **2)
test_SSE
