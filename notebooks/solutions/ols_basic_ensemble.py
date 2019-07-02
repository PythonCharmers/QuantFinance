# Question 1
mask = study_hours < 20
study_hours_cleaned = study_hours[mask]
SAT_scores_cleaned = SAT_scores[mask]  # Don't forget to use the same mask for both X and Y

plt.plot(study_hours_cleaned, SAT_scores_cleaned, 'ro')
plt.xlabel("Hours Studied")
plt.ylabel("SAT Score")

ones_cleaned = np.ones((len(study_hours_cleaned)))
X_cleaned = np.vstack([ones_cleaned, study_hours_cleaned]).T

Y_cleaned = SAT_scores_cleaned.reshape((len(SAT_scores_cleaned), 1))

beta_cleaned = np.linalg.inv(X_cleaned.T.dot(X_cleaned)).dot(X_cleaned.T.dot(Y_cleaned))
print(beta_cleaned)

plt.plot(study_hours_cleaned, SAT_scores_cleaned, 'ro')
plt.xlabel("Hours Studied")
plt.ylabel("SAT Score")

# Here we create x values for "each hour of study" so we can plot the results
x_model = np.arange(0, 25)
y_model = x_model * beta[1] + beta[0]  # Use our learned model to fit the line of best fit.

plt.plot(x_model, y_model, 'b-')


# Question 2

# Store parameter versions here
models = []

n = len(study_hours)

for i in range(100):
    
    # Choose random indexes
    # replace=True is better statistically, we will come back to it later on...
    random_indexes = np.random.choice(np.arange(n), size=int(n/2), replace=True)
    study_hours_sample = study_hours[random_indexes]
    SAT_scores_sample = SAT_scores[random_indexes]
    
    ones_sample = np.ones((len(study_hours_sample)))
    X_sample = np.vstack([ones_sample, study_hours_sample]).T

    Y_sample = SAT_scores_sample.reshape((len(SAT_scores_sample), 1))

    beta_sample = np.linalg.inv(X_sample.T.dot(X_sample)).dot(X_sample.T.dot(Y_sample))
    models.append(beta_sample)
# Average all parameters
final_model = np.mean(models, axis=0)
print(final_model)