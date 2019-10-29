
# 1. We say we reject the null hypothesis, as it has a p value of less than 0.05, i.e. a less than 5% chance of occurring purely by chance.
# 2. The likelihood of the samples given the assumptions is 0.08% (i.e. less than a tenth of 1%).
# 3. No. We are confident the expected value is more than 3.5, but we do not know why (it may be loaded to 5s for instance).


# ### Extended Solution

# $H_0$ The dice rolls 6s, on average, in 1/6 rolls

# $H_A$ The dice rolls 6s, on average, more then 1/6 rolls

# Roll a normal dice 1000 times, and record the number of 6s rolled. Repeat many times.

# Roll the suspected dice 1000 times and record the number of 6s rolled. Repeat many times.

# Perform the `stats.ttest_1samp` test above.
