
from collections import Counter

def confusion_matrix(data):
	
	counts = Counter(tuple(pair) for pair in data)
	print(counts)
	return [[counts[(1, 1)], counts[(1, 0)]],
            [counts[(0, 1)], counts[(0, 0)]]]


data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]
print(confusion_matrix(data))

# TP=ABS(1_PRED/1_TRUE)
# TN=ABS(0_PRED/0_TRUE)
# FP=ABS(0_PRED/1_TRUE)
# FN=ABS(1_PRED/0_TRUE)


[[1, 1], [2, 1]]
