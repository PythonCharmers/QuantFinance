
# Cross validation splits the data into multiple segments, called folds. Commonly, 3 or 10 folds are used.
# We evaluate our model in an iterative test/train split, where each of the fold takes one turn being the "test"
# and all others are the train. Results are then aggregated, such as by taking the mean of the error over all iterations.

# There is an additional test split in the diagram, because we cannot use a fold for evaluation.
# The reason is that these folds are part of the training of the algorithm, and therefore we cannot use them for
# evaluation.
