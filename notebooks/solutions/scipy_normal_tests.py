
stats.normaltest(heights)

stats.kstest(heights, stats.norm.fit(heights).cdf)
