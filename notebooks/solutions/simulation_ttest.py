
import numpy as np

def run_experiment(dof):
    """Runs a single t-value experiment"""
    
    # Create random sizes for each dataset
    n1 = np.random.randint(3, dof + 2 - 1)
    n2 = (dof + 2) - n1
    
    X1 = np.random.randn(n1)
    X2 = np.random.randn(n2)
    
    e1 = np.std(X1) / np.sqrt(n1)
    e2 = np.std(X2) / np.sqrt(n2)
    
    sed = np.sqrt(e1**2 + e2**2)
    
    t_stat = (np.mean(X1) - np.mean(X2)) / sed
    return t_stat

N_EXPERIMENTS = 10000

results = {}

for dof in [5, 10, 20, 50, 100, 500]:
    print("dof", dof)
    results[dof] = {}
    values = [run_experiment(dof) for _ in range(N_EXPERIMENTS)]
    values.sort()  # In place operation
    for p_value in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5]:
        n = int(N_EXPERIMENTS * p_value)
        results[dof][p_value] = values[n]
    print(results[dof])

dof = 500

# Compare to the version implemented in scipy
# NOte that Absolute values of the t test should be used
n1 = 249
n2 = 249
X1 = np.random.randn(n1)
X2 = np.random.randn(n2)

stat, p = stats.ttest_ind(X1, X2)
stat, p

results[dof]

import pandas as pd

tstats = pd.DataFrame(results)

tstats
