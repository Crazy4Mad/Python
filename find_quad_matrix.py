rows, columns = map(int, input("Введите количество строк и количество "
                               "столбцов в матрице:").split())
Matrix = [[0]*columns for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        Matrix[i][j] = input("Введите элемент матрицы (0 или 1):")

for i in range(rows):
    for j in range(columns):
        print(Matrix[i][j], end=' ')
    print()

r, c, length = 0, 0, 0
minimum = min(rows, columns)
for quad_mat_len in range(1, minimum):
    matrix = [['1']*quad_mat_len for j in range(quad_mat_len)]
    founded = False
    for i in range(len(Matrix) - quad_mat_len + 1):
        for j in range((len(Matrix[i])) - quad_mat_len + 1):
           aux = Matrix[i:i+quad_mat_len]
           for k in range(quad_mat_len):
               aux[k] = aux[k][j:j+quad_mat_len]
           if aux == matrix:
               r = i
               c = j
               length = quad_mat_len
               founded = True
               break
        if founded:
            break

print()
print(r + 1, c + 1, length)
