palladium = quandl.get("JOHNMATT/PALL", collapse="monthly") # Monthly Palladium trading price
palladium = palladium[palladium.columns[0]] #We only need one column of data

palladium_delta = palladium.diff()

palladium_ucl = palladium_delta.mean() + 3 * palladium_delta.std()
palladium_lcl = palladium_delta.mean() - 3 * palladium_delta.std()

fig, ax, = plt.subplots(figsize=(12, 12))
palladium_delta.plot(ax=ax)
ax.hlines([palladium_ucl, palladium_lcl], xmin=palladium_delta.index.min(), xmax=palladium_delta.index.max())
