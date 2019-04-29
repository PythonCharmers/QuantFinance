increases = prices.diff()
increase_z_score = (increases - increases.mean())/increases.std()
increase_z_score.dropna(inplace=True)
increase_z_score.head()

print("This analysis shows that AAPL has a 'wider tail' in general.")
print("However, MSFT has much more wild swings that appear rarely.")
alt.Chart(increase_z_score.melt(value_name="z_score_adj_close")).mark_bar(opacity=0.4).encode(
    x=alt.X("z_score_adj_close", bin=alt.Bin(maxbins=30)),
    y=alt.Y('count()', stack=None),
    # column='ticker',
    color='ticker',
)