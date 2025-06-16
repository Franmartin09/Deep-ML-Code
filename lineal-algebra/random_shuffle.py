import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
    if seed is not None:
        np.random.seed(seed)
    idx=np.random.permutation(len(X))
    X[idx]
    y[idx]
    print(X[idx],  y[idx])
    pass 


X = np.array([[1, 2],[3, 4],[5, 6],[7, 8]])
y = np.array([1, 2, 3, 4])

shuffle_data(X,y)