def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        in_matrix = []
        for j in range(m):
            in_matrix.append(value)
        matrix.append(in_matrix)
    print(matrix)


get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
