

# Exercise 1
x_values_1 = np.linspace(-5, 5, 1000)
distributions_1 = [stats.norm(x, 1) for x in x_values_1]
y_1 = np.array([distribution.cdf(1) - distribution.cdf(0)
               for distribution in distributions_1])
plt.plot(x_values_1, y_1)

# Exercise 2
x_values_2 = np.linspace(0.1, 20, 1000)
distributions_2 = [stats.norm(0, x) for x in x_values_2]
y_2 = np.array([distribution.cdf(1) - distribution.cdf(0)
               for distribution in distributions_2])
plt.plot(x_values_2, y_2)
print("This function is *decreasing*, as when the standard deviation is higher, "
      "the normal distribution 'spreads out'.")
