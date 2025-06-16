from cmath import sqrt
def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[complex]:
    # Para una matriz 2x2:
    # λ² - (traza)λ + determinante = 0
    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    discriminant = sqrt(trace**2 - 4*det)
    eigen1 = (-trace + discriminant) / 2
    eigen2 = (-trace - discriminant) / 2

    return sorted([abs(eigen1.real), abs(eigen2.real)], reverse=True)


# [2,1]
# [1,2]

# λ^2−4λ+3=0

output = calculate_eigenvalues([[2, 1], [1, 2]])

print(output)