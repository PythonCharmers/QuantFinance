
def run_experiment(n_datapoints=20, threshold=0.8):
    # Note that all data here is randomly chosen
    x_random = np.random.random(n_datapoints)
    y_random = np.random.random(n_datapoints)
    corr = np.corrcoef(x_random, y_random)[0,1]
    return corr > threshold


def run_many_experiments(n_experiments=100000, n_datapoints=20, threshold=0.8):
    false_positives = 0

    for i in range(n_experiments):
        if run_experiment(n_datapoints=n_datapoints, threshold=threshold):
            false_positives += 1
    return false_positives / n_experiments

# Relationship between data size and FP rate
data_size = np.logspace(1, 7, 7, dtype=np.int)
fp_rate_datapoints = np.fromiter((run_many_experiments(n_datapoints=d) for d in data_size), dtype=np.float32)

plt.plot(data_size, fp_rate_datapoints)
