
def in_cbd(postcodes):
    return [postcode in CBD_POSTCODES for postcode in postcodes]

features2 = features + [in_cbd]

k2 = np.c_[k, 0.25]
k2

assert len(features2) == k2.shape[1]

model2 = MinDivergenceModel(features2, samplespace, vectorized=True)

model2.fit(k2);

assert np.allclose(model2.expectations(), k2, atol=1e-6)

p2 = model2.probdist()

fig, axes = plt.subplots(1, figsize=(12, 5))
plt.plot(samplespace, p2, '.', )
axes.set_xlabel('postcode')
axes.set_ylabel('probability')

# We can see more by using a logarithmic vertical axis:

fig, axes = plt.subplots(1, figsize=(12, 5))
plt.semilogy(samplespace, p2, '.', )
axes.set_xlabel('postcode')
axes.set_ylabel('probability')
