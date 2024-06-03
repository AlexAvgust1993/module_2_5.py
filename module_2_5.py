def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # Количество строк в матрице.
        empty_list = []
        matrix.append(empty_list)
        for j in range(m):  # Количество столбцов
            matrix[i].append(value)

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
