import numpy as np
from numpy.linalg import norm

def cosine_similarity(v1, v2):
	# Implement your code here
    return round(np.dot(v1, v2)/(norm(v1)*norm(v2)),3)



v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))
# 1.0