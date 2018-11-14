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
        max_amount_of_zer, max_zer_row = 0, 0
        for i in range(Matrix_size):
            cur_amount_of_zer = 0
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
                    if cur_elem == 0:
                        cur_amount_of_zer += 1
                        have_zeroes = True
            else:
                break
            if cur_amount_of_zer > max_amount_of_zer:#определяю строку с наибольшим количеством нулей
                max_amount_of_zer = cur_amount_of_zer
                max_zer_row = i


        #в цикле просто нужно сдвигать элемент на Matrix_size - 1 позиций по периметру
        #квадрата, запоминая элемент в ячейке, которой мы присвоили сдвинутое значение,
        #и сдвигаем его по тому же правилу. В результате мы пройдем круг и сдвинем все значения
        if is_ok:
            i = 0
            while i < Matrix_size - i - 1:
                for pos in range(i, Matrix_size - i - 1):
                    cur_row, cur_column = Matrix_size - pos - 1, i
                    cur_value = Matrix[cur_row][cur_column]
                    Matrix[cur_row][cur_column] = Matrix[i][pos]

                    cur_row, cur_column = Matrix_size - cur_column - 1, cur_row
                    cur_value, Matrix[cur_row][cur_column] = Matrix[cur_row][cur_column], cur_value
                    cur_row, cur_column = Matrix_size - cur_column - 1, cur_row
                    cur_value, Matrix[cur_row][cur_column] = Matrix[cur_row][cur_column], cur_value

                    Matrix[i][pos] = cur_value
                i += 1
                pass

            if have_zeroes:
                for i in range(Matrix_size):
                    Matrix[i][max_zer_row], Matrix[i][-1] = \
                    Matrix[i][-1], Matrix[i][max_zer_row]
            else:
                print("No zeroes")

            for i in Matrix:
                for j in i:
                    print('{:<10.4g}'.format(j), end=' ')
                print()

    else:
        is_ok = False
else:
    is_ok = False

if not is_ok:
    print("Incorrect input")
