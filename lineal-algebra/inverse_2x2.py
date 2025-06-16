def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	adj = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
	inverse = [[adj[0][0] / det, adj[0][1] / det],
               [adj[1][0] / det, adj[1][1] / det]]
	return inverse

# inverse = Adj(A) / det(A)
# det(A) = a11 * a22 - a12 * a21
# Adj(A) = 1 / a * a22 - a12 * a21
matrix = [[4, 7], [2, 6]]
# [[0.6, -0.7], [-0.2, 0.4]]
