import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	result=[]
	scores = np.array(scores)
	max_score = np.max(scores)
	for i in scores:
		result.append(round(float(i-max_score- np.log(np.sum(np.exp(scores-max_score)))),4))
	return result


A = np.array([1, 2, 3])
print(log_softmax(A))


# array([-2.4076, -1.4076, -0.4076])
