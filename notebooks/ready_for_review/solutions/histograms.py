# Exercise 1: The wikipedia article is good on this topic: https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem

# Extended exercise

def run_experiment(data, target_variable_name='target', sample_size=100):
    """Fits an OLS to the data, predicting the target from all other variables
    """
    sample = data.sample(sample_size)
    
    column_names = [col for col in data.columns if col != target_variable_name]
    # Create formula, predicting target from the sum of all others
    formula = "{} ~ {}".format(target_variable_name, str.join(" + ", column_names))
    model = smf.ols(formula=formula, data=sample).fit()
    
    return model.params


# example: 
print(run_experiment(boston))

# Run many times, join results in a dataframe
results = pd.concat([run_experiment(boston) for i in range(100)], axis=1)

columns = results.index.values
n_columns = len(columns)

n_columns

n_rows, n_cols = 5, 3

# Output histogram plot for each varaible
# A plot with n_rows rows, n_cols cols, and sized so each is 5 by 3 (inches)
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(n_cols * 5, n_rows * 3))

for row in range(n_rows):
    for col in range(n_cols):
        plot_number = (row * n_cols) + col
        if plot_number >= n_columns:
            break 
        column_name = columns[plot_number]
        ax = axes[row, col]
        ax.set_title(column_name)
        
        ax.hist(results.loc[column_name], bins=30)
        