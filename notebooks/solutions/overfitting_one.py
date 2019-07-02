# 50 points randomly from 0 to 100
x_test = np.random.random(50) * 100
error_test = np.random.randn(len(x_test)) * 5
y_test = x_test * 3 + 1 + error_test

# Training errors
SSE_linear = np.sum((y_pred_linear - y) ** 2)
SSE_overfit = np.sum((y_pred_overfit - y) ** 2)

print(SSE_linear, SSE_overfit)  # Overfit is lower for training error

plt.plot(x_test, y_test, 'go', alpha=0.5)

y_est_linear = model(x_test)
y_est_poly = model_30(x_test)

# Training errors
SSE_est_linear = np.sum((y_est_linear - y_test) ** 2)
SSE_est_overfit = np.sum((y_est_poly - y_test) ** 2)

print(SSE_est_linear, SSE_est_overfit)  # SSE is **very** high for the overfit model.
