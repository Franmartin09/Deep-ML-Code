def matrixmul(a:list[list[int|float]], b:list[list[int|float]]) -> list[list[int|float]]:
	if len(a[0]) != len(b):
		return -1
	# Inicializamos la matriz resultado con ceros
	result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

	# Multiplicación de matrices
	for i in range(len(a)):  # filas de A
		for j in range(len(b[0])):  # columnas de B
			for k in range(len(b)):  # columnas de A == filas de B
				result[i][j] += a[i][k] * b[k][j]

	return result


A = [[1,2],[2,4]]
B = [[2,1],[3,4]]
# [[ 8,  9],[16, 18]]
i=0
j=0
# [1,2] [2,1]
# [2,4] [3,4]
print(matrixmul(A,B))



# multiply two matrices together (return -1 if shapes of matrix dont aline), i.e. C=A⋅B
# Reasoning:
# 1*2 + 2*3 = 8; 2*2 + 3*4 = 16; 1*1 + 2*4 = 9; 2*1 + 4*4 = 18
# Example 2: input: A = [[1,2], [2,4]], B = [[2,1], [3,4], [4,5]] output: -1 reasoning: the length of the rows of A does not equal the column length of B