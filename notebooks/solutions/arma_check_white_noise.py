
def check_white_noise(data: np.ndarray):
    # check mean 0
    _, p_mean = stats.ttest_1samp(data, 0)
    if p_mean > 0.05:
        print('data has mean of 0 (unable to reject)')
    else:
        print('data does not have a mean of 0!')
    # check homeoskedastic
    _, p_skedastic = stats.levene(*data.reshape(2, -1))
    if p_skedastic > 0:
        print('data is homeoskedastic (unable to reject)')
    else:
        print('data is HETEROskedastic!')
    # plot to check for autocorrelation
    pd.plotting.autocorrelation_plot(data)
    plt.title('autocorrelation plot')
    plt.show()

print('Training results:')
check_white_noise(train_residuals)
print('Testing results:')
check_white_noise(np.r_[0, test_residuals])
