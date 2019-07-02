
# Exercise
# There is a 95% chance of "not a positive result", so for two experiments , we need both to be "not positive"
# The chance of this is 95% times 95% which is 0.95 * 0.95 = 0.9025, approximately 90%, so we have about a 10%
# chance of getting a positive result from at least one of our tests.

# For ten experiments, that drops to 0.95^10 = 0.59 for "all not positive", about a 40% chance of "at least one positive"
0.95 ** 20
# For twenty experiments, we have a 0.95^20 = 0.36 for "all not positive"
# about a 64% chance of at least one being positive - so it's *more* likely to get a positive result than not

# Extended exercise

import numpy as np

def get_sample_mean(n_random=100):
    sample = np.random.randn(n_random)
    return sample.mean()

N_TESTS = 10000

means = np.array([get_sample_mean() for i in range(N_TESTS)])

plt.hist(means)  # Normal distribution, as expected


np.sum(means > 0.166)
