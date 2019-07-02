# Exercise 1
print(B.shape)  # Shape is (3, 2), so V2 must be (2, 1)
V2 = np.array([1, 2])  # Shape is (2,), NumPy figures out the rest, but the result is the wrong shape:

result1 = B.dot(V2)
print(result1, result1.shape)

result2 = B.dot(V2.reshape(-1, 1))

print(result2, result2.shape)  # Better shape for future matrix multiplication

B

# Exercise 2
B.dot(np.ones(shape=(2, 1)))  # Note: row-wise sum

# Exercise 3
B.T  # Rotates by 90 degress. Rows become columns, columns become rows