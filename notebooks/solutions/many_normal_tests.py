from statsmodels import api as sm
from statsmodels.stats import stattools

max_sample_size = 200
distribution = stats.norm()


sample_size_values = np.linspace(10, max_sample_size, 20, dtype=np.int)
results = []  # Store all results here

for sample_size in sample_size_values:

    scipy_normal_test_passed = 0
    scipy_kstest_passed = 0
    statsmodels_kstest_passed = 0
    statsmodels_jarque_bera_passed = 0
    
    for i in range(1000):
        data = distribution.rvs(sample_size)
        
        # scipy normaltest
        stat, p = stats.normaltest(data)
        if p > 0.05:
            scipy_normal_test_passed += 1
        
        # scipy kstest
        stat, p = stats.kstest(data, 'norm')
        if p > 0.05:
            scipy_kstest_passed += 1
            
        # statsmodels kstest
        statistic, p_value = sm.stats.diagnostic.kstest_normal(data)
        if p_value > 0.05:
            statsmodels_kstest_passed += 1
            
        # statsmodels jarque_bera
        jbstat, pvalue, skew, kurtosis = stattools.jarque_bera(data)
        if pvalue > 0.05:
            # Same as scipy.normaltest!
            statsmodels_jarque_bera_passed += 1

    row = [scipy_normal_test_passed, scipy_kstest_passed, statsmodels_kstest_passed, statsmodels_jarque_bera_passed]
    
    results.append(row)

results = np.array(results)  # Convert to NumPy for fancy indexing

plt.plot(sample_size_values, results[:,0], alpha=0.5, label='scipy.normaltest')
plt.plot(sample_size_values, results[:,1], alpha=0.5, label='scipy.kstest')
plt.plot(sample_size_values, results[:,2], alpha=0.5, label='statsmodels.kstest_normal')
plt.plot(sample_size_values, results[:,3], alpha=0.5, label='statsmodels.jarque_bera')
plt.legend(bbox_to_anchor=(1.05, 1.0))
