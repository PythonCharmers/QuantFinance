#1

distribution = stats.normal(0, 1)

x_values = np.linspace(-3, 3, 1000)
y = distribution.pdf(x_values)
plt.plot(x_values, y)

#2 
distribution = stats.uniform(-2, 4)

x_values = np.linspace(-3, 3, 1000)
y = distribution.pdf(x_values)
plt.plot(x_values, y)
print("The expected value for a uniform distribution is E[x] = (a + b) / 2")