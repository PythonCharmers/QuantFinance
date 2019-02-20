
# Question 2 answer

def plot_histogram_normal(mean, standard_deviation):
    distribution = stats.norm(mean, standard_deviation)
    normal_values = pd.DataFrame({"value": distribution.rvs(10000)})

    chart = alt.Chart(normal_values).mark_bar().encode(
        alt.X("value", bin=alt.Bin(maxbins=100)),
        'count()'
    )
    return chart


# Same function, but with colour as an option
def plot_histogram_normal(mean, standard_deviation, color):
    distribution = stats.norm(mean, standard_deviation)
    normal_values = pd.DataFrame({"value": distribution.rvs(10000)})

    chart = alt.Chart(normal_values).mark_bar().encode(
        alt.X("value", bin=alt.Bin(maxbins=100)),
        y='count()',
        color=alt.value(color)
    )
    return chart

chart1 = plot_histogram_normal(1, 7, color="#8b8378")

chart1  # Running just "chart1" in a Jupyter Notebook cell will show the chart

chart2 = plot_histogram_normal(10, 1, color="#cd5c5c")

chart3 = plot_histogram_normal(-10, 5, color="#9acd32")

chart1 + chart2 + chart3  # Running this in it's own cell will show all three charts overlaid