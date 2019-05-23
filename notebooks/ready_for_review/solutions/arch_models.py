
y = np.zeros(1000)
np.random.seed(42)

y[0] = np.random.normal()
for i in range(1, len(y)):
    y[i] = np.random.normal() * np.sqrt(5 + 0.5 * y[i-1]**2) + np.sqrt(5 + 0.2 * y[i-3]**2)

#Try with default, GARCH(1,1)
model = arch_model(y)
results.summary()

#Retry with GARCH(2,2)
model = arch_model(y,vol="GARCH", p=2, q=2)
result = mod.fit()
result.summary()



