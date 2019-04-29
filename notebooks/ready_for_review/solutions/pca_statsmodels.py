
from statsmodels.multivariate.pca import PCA

model = PCA(X)

transformed = model.transformed_data

components = model.eigenvecs

components
