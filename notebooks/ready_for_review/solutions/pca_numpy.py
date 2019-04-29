# Solution to extended exercise, 
# based on https://medium.com/100-days-of-algorithms/day-92-pca-bdb66840a8fb

def PCA(X, n_components):
    # normalize to zero mean
    mu = X.mean(axis=0)
    X = X - mu
    
    # eigenvectors of covariance matrix
    sigma = X.T @ X
    eigvals, eigvecs = np.linalg.eig(sigma)
    
    # principal components
    order = np.argsort(eigvals)[::-1]
    components = eigvecs[:, order[:n_components]]
    
    # projection
    Z = X @ components
    
    # result
    return Z, components
