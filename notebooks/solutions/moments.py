# Exercise 1
aapl['Gain'] = aapl['Close'] - aapl['Open']

# Exercise 2
alt.Chart(aapl).mark_bar().encode(
        alt.X("Gain", bin=alt.Bin(maxbins=100)),
        y='count()'
)

# Exercise 3
skew = stats.skew(aapl['Gain'])
print("The skew is {}".format(skew))
kurtosis = stats.kurtosis(aapl['Gain'])
print("The kurtosis is {}".format(kurtosis))