def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    res=[]
    for i in range(0,len(a[0])): #0 -> 2
        aux=[]
        for j in range(0,len(a)): #0 -> 1
            aux.append(a[j][i])
        res.append(aux)
    return res


# [[1,4],[2,5],[3,6]]
a = [[1,2,3],[4,5,6]]

output = transpose_matrix(a)
# output = matrix_dot_vector([[1, 2], [2, 4]], [1, 2])
# output = matrix_dot_vector([[1, 2], [2, 4], [3, 5]], [1, 2])
print(output)
