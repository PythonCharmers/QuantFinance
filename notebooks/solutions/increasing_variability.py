
y_increasing = np.random.random(len(x)) * np.arange(len(x)) * 25  # Your equation may vary

plt.plot(x, y_increasing, 'bo')

fit_linear_plot_residuals(x, y_increasing)
