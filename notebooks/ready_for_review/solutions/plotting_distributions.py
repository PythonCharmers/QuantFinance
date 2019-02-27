

# Exercise 1
def calculate_mean_of_random_iterations(distribution, n_random=10000):
    """Computes 10,000 random values from a given distribution and returns the mean"""
    random_values = distribution.rvs(n_random)
    return random_values.mean()

distributions = dict([("normal", stats.norm()),
                 ("gamma", stats.gamma(0.5)),
                 ("uniform", stats.uniform(0, 1))
                ])

for distribution_name, distribution in distributions.items():
    print(distribution_name, calculate_mean_of_random_iterations(distribution))

def create_many_means(distribution, n_iterations=1000):
    """Performs many iterations of `calculate_mean_of_random_iterations` and records the values"""
    # Note: you can do this with a list comprehension. A rolled out loop
    # is used here for clarity
    means = []
    for iteration in range(n_iterations):
        means.append(calculate_mean_of_random_iterations(distribution))
    return means

means = pd.DataFrame({distribution_name: create_many_means(distribution)
                    for distribution_name, distribution in distributions.items()})
data = pd.melt(means, var_name='Distribution', value_name='Sample Mean')

charts = {}

for distribution_name in distributions:
    print(distribution_name)
    current_data = data[data["Distribution"] == distribution_name]
    cur_chart = alt.Chart(current_data).mark_area(
                    opacity=0.3,
                    interpolate='step'
                ).encode(
                    alt.X('Sample Mean', bin=alt.Bin(maxbins=100)),
                    alt.Y('count()', stack=None),
                    alt.Color(
                        'Distribution',
                        scale=alt.Scale(range=['#0000ff', '#008000', '#ff0000'])
                    ),
                )
    charts[distribution_name] = cur_chart


alt.layer(*charts.values()).resolve_scale(x='independent')