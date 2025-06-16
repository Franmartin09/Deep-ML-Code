import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	if y is None:
		return [X[i:i + batch_size] for i in range(0, len(X), batch_size)]
	else:
		return [[X[i:i + batch_size], y[i:i + batch_size]] for i in range(0, len(X), batch_size)]


X = np.array([[1, 2], 
			[3, 4], 
			[5, 6], 
			[7, 8], 
			[9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))


# [  [ [[1, 2], [3, 4]], [1, 2] ], [ [[5, 6], [7, 8]], [3, 4] ], [ [[9, 10]], [5] ]  ]