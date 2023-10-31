def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if cols1 != rows2:
        print("Error: The number of columns in the first matrix should be equal to the number of rows in the second matrix.")
        return None
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
# Sample input matrices
mat1 = [[1, 2],
        [5, 3]]

mat2 = [[2, 3],
        [4, 1]]
result = matrix_multiplication(mat1, mat2)
for row in result:
    print(row)
