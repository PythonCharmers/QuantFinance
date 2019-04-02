import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt

def fit_linear_plot_residuals(x, y):
    """Fits a linear model and plots a residual plot"""
    X = sm.add_constant(x)
    model = sm.OLS(y, X)  # Capital X, which has constants already
    results = model.fit()
    y_pred = results.predict(X)

    errors = y_pred - y
    plt.plot(x, errors, 'ro')
    plt.hlines(0, xmin=x.min(), xmax=x.max())
