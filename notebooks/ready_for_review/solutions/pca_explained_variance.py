
# Fit a PCA model to the data
full_pca = PCA(n_components=64)
full_pca.fit(X)

# Plot the cumulative sum
plt.plot(np.cumsum(full_pca.explained_variance_ratio_))
