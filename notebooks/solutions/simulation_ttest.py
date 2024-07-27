from math import floor, ceil
import numpy as np
import pandas as pd

def run_experiment(dof):
    """Runs a single t-value experiment"""
    
    n1 = floor(dof/2) + 1
    n2 = ceil(dof/2) + 1

    assert(dof == n1 + n2 - 2)
    
    X1 = np.random.randn(n1)
    X2 = np.random.randn(n2)
    
    e1 = np.std(X1) / np.sqrt(n1)
    e2 = np.std(X2) / np.sqrt(n2)
    
    sed = np.sqrt(e1**2 + e2**2)
    
    t_stat = abs((np.mean(X1) - np.mean(X2)) / sed)
    return t_stat

N_EXPERIMENTS = 10000
dofs = [5, 10, 20, 50, 100]
p_values = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]

results = {}

for dof in dofs:
    results[dof] = {}
    values = [run_experiment(dof) for _ in range(N_EXPERIMENTS)]
    values.sort(reverse=True)  # In place operation
    for p_value in p_values:
        n = int(N_EXPERIMENTS * p_value)
        results[dof][p_value] = values[n-1]
    
results = pd.DataFrame.from_dict(results)
print(results)

# Check our results:
from scipy.special import stdtrit

true_results = {}
for dof in dofs:
    true_results[dof] = {}
    for p_value in p_values:
        true_results[dof][p_value] = stdtrit(dof, 1 - p_value / 2)

true_results = pd.DataFrame.from_dict(true_results)
print(true_results)
