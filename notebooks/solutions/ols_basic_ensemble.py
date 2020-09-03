# Question 1
mask = cash_rate < 6
cash_rate_cleaned = cash_rate[mask]
house_prices_cleaned = house_prices[mask]  # Don't forget to use the same mask for both X and Y

plt.plot(cash_rate_cleaned, house_prices_cleaned, 'ro')
plt.xlabel("Cash Rate")
plt.ylabel("SAT Score")

ones_cleaned = np.ones((len(cash_rate_cleaned)))
X_cleaned = np.vstack([ones_cleaned, cash_rate_cleaned]).T

Y_cleaned = house_prices_cleaned.reshape((len(house_prices_cleaned), 1))

beta_cleaned = np.linalg.inv(X_cleaned.T.dot(X_cleaned)).dot(X_cleaned.T.dot(Y_cleaned))
print(beta_cleaned)

plt.plot(cash_rate_cleaned, house_prices_cleaned, 'ro')
plt.xlabel("Cash Rate")
plt.ylabel("House Prices")

# Here we create x values for "each hour of study" so we can plot the results
x_model = np.arange(0, 8, 0.25)
y_model = x_model * beta[1] + beta[0]  # Use our learned model to fit the line of best fit.

plt.plot(x_model, y_model, 'b-')

# Question 2

# Store parameter versions here
models = []

n = len(cash_rate_cleaned)

for i in range(100):
    
    # Choose random indexes
    # replace=True is better statistically, we will come back to it later on...
    random_indexes = np.random.choice(np.arange(n), size=int(n/2), replace=True)
    cash_rate_sample = cash_rate[random_indexes]
    house_prices_sample = house_prices[random_indexes]
    
    ones_sample = np.ones((len(cash_rate_sample)))
    X_sample = np.vstack([ones_sample, cash_rate_sample]).T

    Y_sample = house_prices_sample.reshape((len(house_prices_sample), 1))

    beta_sample = np.linalg.inv(X_sample.T.dot(X_sample)).dot(X_sample.T.dot(Y_sample))
    models.append(beta_sample)
# Average all parameters
final_model = np.mean(models, axis=0)
print(final_model)