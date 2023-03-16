

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

# Extended Exercise

# options for one dice
opts = np.arange(1, 7)
# all combinations of first dice and second dice, flattened and counted the frequency
nums, counts = np.unique((opts[None] + opts[:, None]).flatten(), return_counts=True)
# add 0 probability options on either end of distribution
nums = np.concatenate(([nums.min()-1], nums, [nums.max()+1]))
probs = np.concatenate(([0], counts / counts.sum(), [0]))  # this only holds true for uniform distribution
csum = np.cumsum(probs)

# add steps and plot
plt.plot(
    np.stack([nums, nums]).T.flatten()[1:],
    np.stack([csum, csum]).T.flatten()[:-1]
)
plt.xlabel('sum')
plt.ylabel('p(sum <= value)')
