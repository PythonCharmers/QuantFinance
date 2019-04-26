
# Question 1
# You wouldn't use the actual error, as the "negative" errors would cancel out the positive errors
raw_error = np.sum(predicted_scores - SAT_scores)
print(raw_error)  # note how "small" this is, compared to the absolute error


# Question 2
# (beta, intercept)
models = [(30, 300),
          (20, 250),
          (40, 400)]

best_error = None
best_model = None

for model in models:
    print("Model is: {}".format(model))
    b, c = model
    predicted_scores = study_hours * b + c  # Same values as before - this is our "model"
    squared_error = np.sum((predicted_scores - SAT_scores) ** 2)
    print(" The squared error is {:.2f}".format(squared_error))
    
    if best_error is None or squared_error < best_error:
        best_error = squared_error
        best_model = model
        
print("The best model was {}".format(best_model))