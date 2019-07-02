# Rolling Forecast Origin Function
def rolling_forecasting_origin(time_series, m=1):
    """Performs a rolling forecasting origin with steps of m

    parameters:
        time_series: pandas data frame with a time series index
        m: positive non-zero integer. 1 by default 

    returns:
        folds: a list of each of the training and testing folds for pandas.
    """

    idx_max = len(time_series)
    iters = np.arange(1, idx_max - m + 1)
    folds = [[[0],m]] # np.arange does not return a valid result, so start from 1
    
    for i in iters:
        train_fold = np.arange(0, i + 1)
        test_fold = min(i + m, idx_max)
        folds.append([train_fold, test_fold])
    
    return folds

# Let's test our function!
dates = np.array('2015-07-04', dtype=np.datetime64) + np.arange(100)
dates
rolling_forecasting_origin(date, 10)

# Here is essentially the same function code, but presented as a python generator which 
# can be iterated over, for example in a for loop.
def rolling_forecasting_origin_generator(time_series, m=1):
    """Performs a rolling forecasting origin with steps of m

    parameters:
        time_series: pandas data frame with a time series index
        m: positive non-zero integer. 1 by default 

    returns:
        folds: a list of each of the training and testing folds for pandas.
    """

    idx_max = len(time_series)
    iters = np.arange(1, idx_max - m + 1)
    folds = [[[0],m]] # np.arange does not return a valid result, so start from 1
    
    for i in iters:
        train_fold = np.arange(0, i + 1)
        test_fold = min(i + m, idx_max)
	# yield returns a value, but does not end our function, it will resume when the
	# next value is called for, running the next iteration of our for loop.
        yield [train_fold, test_fold]  
        
    #When we reach return, our generator is exhausted.
    return




