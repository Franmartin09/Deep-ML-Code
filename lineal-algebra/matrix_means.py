def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means=[]
    if mode=='column':
        for i in range(len(matrix)):
            lenght = len(matrix[i])
            value = 0
            for j in range(len(matrix[i])):
                value += matrix[j][i]
            means.append(value/lenght)
    elif mode=='row':
        for i in range(len(matrix)):
            value = 0
            for j in range(len(matrix[i])):
                value += matrix[i][j]
            means.append(value/len(matrix[i]))
    return means


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
mode = 'row'

output = calculate_matrix_mean(matrix, mode)

print(output)