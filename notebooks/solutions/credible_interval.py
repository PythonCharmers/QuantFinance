def shortest_interval(posterior, alpha=0.05, sensitivity=.01):
    """
    A (1 - α) credible interval
    
    Parameters
    ----------
    posterior : function
        A posterior probability density function (normalized)
    
    alpha : float
        A significance level (of sorts)
        
    Returns
    -------
        A tuple (lower, upper) giving the lower and upper bounds for
        the (1 - α) credible interval
    """
    
    curr_prob = 0.0
    target = 1 - alpha
    min_length = 1
    optimal_start = 0
    
    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < 1):
 
        # Increase upper bound while
        # sum is smaller than or equal to 1-a
        while (curr_prob <= target and end < 1):
            end += sensitivity
            curr_prob, err = integrate.quad(posterior, start, end)
            
 
        # If current sum becomes greater than x
        # start increasing lower bound, and save 
        # smallest interval.
        while (curr_prob > target and start < 1):
             
            # new min length and new start
            if min_length > (end - start):
                min_length = end - start
                optimal_start = start
            
            start += sensitivity
            curr_prob, err = integrate.quad(posterior, start, end)
         
 
    return (optimal_start, optimal_start+min_length)

beta = scipy.stats.beta(100,200)
low, high = hpd(beta.pdf, alpha=.10, sensitivity=.005)
beta.cdf(high) - beta.cdf(low) #this is equal to 1-a