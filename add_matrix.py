def matrix_addition(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result

mat1 = [[1, 2], [5, 3]]
mat2 = [[2, 3], [4, 1]]

result = matrix_addition(mat1, mat2)

for row in result:
    print(row)
