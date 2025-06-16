import numpy as np
from typing import Tuple

def feature_scaling(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
	# Your code here
	suma=[]
	for i in data:
		suma.append(np.sum(i))
	print(suma)
	print(np.std(suma))
	print(np.std(data))
	print(np.std(np.mean(data, keepdims=True)))
	standardized_data=np.ndarray
	normalized_data=np.ndarray
	return (standardized_data, normalized_data)

data = np.array([[1, 2], [3, 4], [5, 6]])

print(feature_scaling(data))

# ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])

