""
# 1. Use the np.arange and np.reshape functions to create a square matrix
S = np.arange(16).reshape(4, 4)
print(S)

# 2. Use the np.diag function to create a diagonal matrix
D = np.diag([1, 2, 3])
print(D)

# 3. Use the np.eye function to create an identity matrix
I = np.eye(4)
print(I)

# 4. Create a scalar matrix
C = np.eye(4) * 5
print(C)

# 5. Use the np.zeros function to create a null matrix of size 4 by 5
N = np.zeros(shape=(4, 5))
print(N)