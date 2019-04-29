
# combined comes from previous data

def compute_lagged_correlation(combined, lag=1):
    combined['Lagged Inflation'] = combined['Inflation'].shift(lag)
    return combined.corr().loc[('Cash Rate', "Lagged Inflation")]

lag = list(range(-12, 13, 1))
lagged_correlation = pd.Series([compute_lagged_correlation(combined, lag=lag) for lag in lag], index=lag)
lagged_correlation.index.name = "Lag"
lagged_correlation.name = "Cross Correlation"

lagged_correlation.plot();

# Answer to question:
# The -1 to -3 lag indicates that the cash rate appears to change in response to inflation, 
# rather than the other way around.