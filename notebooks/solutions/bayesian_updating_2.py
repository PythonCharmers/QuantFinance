# Both exercises solved here, see commetns for question numbers
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 15, 50, 500, 5000]  # Exercise 1 - added 5000 (removed 8 to make plots line up)
data = stats.bernoulli.rvs(0.8, size=n_trials[-1])  # Exercise 2 - biased coin
x = np.linspace(0, 1, 100)

# For the already prepared, I'm using Binomial's conj. prior.
for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials)/2, 2, k+1)
    plt.xlabel("$p$, probability of heads") \
        if k in [0, len(n_trials)-1] else None
    plt.setp(sx.get_yticklabels(), visible=False)
    heads = data[:N].sum()
    y = dist.pdf(x, 1 + heads, 1 + N - heads)
    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)


plt.suptitle("Bayesian updating of posterior probabilities",
             y=1.02,
         fontsize=14)

plt.tight_layout()
