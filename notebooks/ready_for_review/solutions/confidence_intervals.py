# 1 & 2
d = data.reset_index().dropna()
d["std"] = np.std(d["InterestRate"]) # Add a column for std

import altair as alt

# the base chart
base = alt.Chart(d).transform_calculate(
    ymin="datum.InterestRate-datum.std",
    ymax="datum.InterestRate+datum.std"
)
# Data Line
line = base.mark_line().encode(x="Date", y="InterestRate")
# Error Bars
bar = base.mark_errorbar().encode(x="Date", y="ymin:Q", y2="ymax:Q")
line + bar


# 3
from math import sqrt
pool = data["InterestRate"].dropna()

sample_size = int(len(pool)/5)
iters = range(1000)
means = []

for i in iters:
    sample = np.random.choice(pool, sample_size)
    means.append(np.mean(sample))

mu = np.mean(means)
std = np.std(means)
stats.norm.interval(0.95, loc=mu, scale=std/sqrt(1000))

# 4 
pool = data["InterestRate"].dropna()

sample_size = int(len(pool)/5)
iters = range(1000)
means = []

for i in iters:
    sample = np.random.choice(pool, sample_size)
    means.append(np.mean(sample))

idx_lower = int(len(means)*.025)
idx_upper = int(len(means)*.975)
sorted_means = np.sort(means)
lower = sorted_means[idx_lower]
upper = sorted_means[idx_upper]
lower, upper
