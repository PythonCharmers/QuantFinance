
# Mean not 0

X = np.random.random(100) + 10  # Mean is about 10.5

plt.plot(X)

pd.plotting.autocorrelation_plot(X)

# Variance not constant

i = np.arange(100)
X = np.random.random(len(i)) * i

plt.plot(X)

pd.plotting.autocorrelation_plot(X)

# Lagged correlation
X = [1] * 100
for i in range(1, 100):
    X[i] = X[i-1] * np.random.random() * 2
    
plt.plot(X)

pd.plotting.autocorrelation_plot(X)
