def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    result = []
    for i in vectors:
        cov_feat=[]
        for j in range(len(i[:-1])):
            cov_feat.append(float(abs(i[j]-i[j+1])))
        result.append(cov_feat)
    return result

# output = calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]])
# output: [[1.0, 1.0], [1.0, 1.0]]

output = calculate_covariance_matrix([[1, 5, 6], [2, 3, 4], [7, 8, 9]])
print(output)
# output : [[7.0, 2.5, 2.5], [2.5, 1.0, 1.0], [2.5, 1.0, 1.0]]



# [1, 2, 3]      ->     [1.0, 1.0]
# [4, 5, 6]      ->     [1.0, 1.0]

