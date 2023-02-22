import numpy as np
from sklearn.datasets import make_friedman1
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA

def pca_transform(pca, X):
    pca.fit(X)
    X_transformed = pca.transform(X)
    
# Generate datasets    
X, _ = make_friedman1(n_samples=10000, n_features=1000, random_state=0)
sparse_X = np.diag(np.random.normal(size=1000))

# Different kinds of PCA
pca = PCA(n_components=2, svd_solver= 'full')
randomizedpca = PCA(n_components=2, svd_solver= 'randomized')
sparsepca = SparsePCA(n_components=2, random_state=0)

# Evaluate on a normal dataset
%time pca_transform(pca, X)
%time pca_transform(randomizedpca, X) # Fastest
%time pca_transform(sparsepca, X)  # it would cost too much time

# Evaluate on a sparse dataset
%time pca_transform(pca, sparse_X)
%time pca_transform(randomizedpca, sparse_X) # still Fastest
%time pca_transform(sparsepca, sparse_X)  