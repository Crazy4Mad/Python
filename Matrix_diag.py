Matrix_size = input("Enter a size of matrix:")
integer_masks = [' ', ' e ']
full_masks = [' ', '- ', ' e ', '- e ', ' e- ', '- e- ',
              ' . e ', '- . e ', ' . e- ', '- . e- ', '. e ',
              '. e- ', '. ', ' .', ' . ']#маски на все возможные строки, которые можно
                                         #привести к типу float
cur_mask = ''
first_dial = True
have_zeroes = False #флаг нужен для того, чтобы понимать, нужно ли удалять столбец или нет
for elem in Matrix_size:
    if elem <= '9' and elem >= '0':#проверяем, является ли текущей элемент введенной строки цифрой
        if first_dial:
            first_dial = False
            cur_mask += ' '
    else:
        first_dial = True
        cur_mask += elem

if cur_mask in integer_masks:
    Matrix_size = int(Matrix_size)
    if Matrix_size > 0:
        Matrix = [[0]*Matrix_size for i in range(Matrix_size)]#создаем нулевую матрицу заданного размера
        to_go = Matrix_size**2#счетчик оставшегося количества элементов, которые нужно ввести
        is_ok = True
        if Matrix_size == 0:
            is_ok = False
        for i in range(Matrix_size):
            if is_ok:
                for j in range(Matrix_size):
                    cur_elem = input("Enter the element:")
                    cur_mask = ''
                    first_dial = True
                    for elem in cur_elem:
                        if elem <= '9' and elem >= '0':
                            if first_dial:
                                first_dial = False
                                cur_mask += ' '
                        else:
                            first_dial = True
                            cur_mask += elem
                    if cur_mask not in full_masks:
                        is_ok = False
                        break
                    to_go -= 1
                    print(to_go, "element(s) more")
                    cur_elem = float(cur_elem)
                    Matrix[i][j] = cur_elem
            else:
                break

        if is_ok:
            max_diag_sum, max_diag_elem = Matrix[0][0], 0
            for column_begin in range(Matrix_size):
                cur_sum = 0
                for row in range(column_begin + 1):
                    cur_sum += Matrix[row][column_begin - row]
                if max_diag_sum < cur_sum:
                    max_diag_sum = cur_sum
                    max_diag_elem = column_begin

                cur_sum = 0
                for row in range(column_begin + 1):
                    cur_sum += Matrix[Matrix_size-row - 1][Matrix_size-1-
                                                    (column_begin - row)]
                if max_diag_sum < cur_sum:
                    max_diag_sum = cur_sum
                    max_diag_elem = column_begin

            for i in range(Matrix_size):
                for j in range(Matrix_size):
                    if Matrix[i][j] > max_diag_sum:
                        Matrix[i][j] = 0

            for i in range(Matrix_size):
                for j in range(Matrix_size):
                    print("{:<10.6g}".format(Matrix[i][j]), end=' ')
                print()
if not is_ok:
    print("Incorrect input")
