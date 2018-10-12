from math import sqrt

def y1(x):
    return x**3 - 2*x**2 + 4*x - 8

def y2(x):
    return 1 - 1/x**2

def y3(x):
    return sqrt(abs(y1(x)*y2(x)))

from_x, to_x, pace_x = map(float, input("Enter the first and the last"\
                        " x-coordinates and a pace dividing them by a"\
                                        " space:").split())

#переменные для динамического вычисления отступов, границ, значений в табличке
dials_precision = "%10.6g" #точность числа
index = dials_precision.find('.') #получаю позицию '.', чтобы потом считать целую часть от числа после%

#оставшиеся переменные введены для минимизации вычислений (часто используются)
spaces_in_the_title = int((int(dials_precision[1:index])) / 2)
length_of_table_lower_bound = (int(dials_precision[1:index]) + 2) * 4 + 5
left_am_of_spaces, right_am_of_spaces, delimiter = int(spaces_in_the_title +\
                    (spaces_in_the_title * 2 < int(dials_precision[1:index]))),\
                    spaces_in_the_title, ' '
is_sequence_decreasing = to_x - from_x < 0

if (pace_x != 0) and (to_x - from_x)*pace_x >= 0 and abs(to_x - from_x)\
        >= abs(pace_x):
    min_y1_value, max_y1_value, x_copy = y1(from_x), y1(from_x), from_x
    negative_value_exists = False

    #специльным образом отформатированный вывод всех значений в строку
    print("|" + (left_am_of_spaces + 1) * delimiter + 'x'
          + right_am_of_spaces * delimiter + '|' +
          left_am_of_spaces * delimiter + "y1" + right_am_of_spaces * delimiter\
          + '|' + left_am_of_spaces * delimiter + 'y2'\
          + right_am_of_spaces * delimiter + '|' + left_am_of_spaces * delimiter\
          + "y3" + right_am_of_spaces * delimiter + "|\n"\
          + length_of_table_lower_bound * '-')

    while(is_sequence_decreasing and x_copy >= to_x) or\
         (not is_sequence_decreasing and x_copy <= to_x):
        y1_cur_value = y1(x_copy)
        min_y1_value = (min_y1_value > y1_cur_value) * y1_cur_value + \
                       (min_y1_value <= y1_cur_value) * min_y1_value
        max_y1_value = (max_y1_value < y1_cur_value) * y1_cur_value + \
                       (max_y1_value >= y1_cur_value) * max_y1_value
        negative_value_exists += y1_cur_value < 0

        aux_x = dials_precision%x_copy
        aux_y1 = dials_precision%y1_cur_value

        aux = len(aux_x) != int(dials_precision[1:index]) + 2
        print('|' + delimiter*aux + aux_x + delimiter*aux + '|', end='')

        aux = len(aux_y1) != int(dials_precision[1:index]) + 2
        print(delimiter*aux + aux_y1 + delimiter*aux + '|', end='')

        if (x_copy != 0):
            aux_y2 = dials_precision % y2(x_copy)
            aux = aux = len(aux_y2) != int(dials_precision[1:index]) + 2
            print(delimiter * aux + aux_y2 + delimiter * aux + '|', end='')

            aux_y3 = dials_precision % y3(x_copy)
            aux = len(aux_y3) != int(dials_precision[1:index]) + 2
            print(delimiter*aux + aux_y3 + delimiter*aux +\
                  "|\n" + length_of_table_lower_bound * '-')
        else:
            print((left_am_of_spaces - 2) * delimiter + "не сущ"\
                 + (right_am_of_spaces - 2) * delimiter + '|' \
                 + (left_am_of_spaces - 2) * delimiter + "не сущ"\
                 + (right_am_of_spaces - 2) * delimiter + "|\n" \
                 + length_of_table_lower_bound * '-')

        x_copy += pace_x



    #график
    print('\n\n','\t\t', "График функции y1 = x**3 - 2*x**2 + 4*x - 8", '\n')
    print((int(dials_precision[1:index]) + 2) * ' ' + 82 * ' ' + 'y')
    print((int(dials_precision[1:index]) + 2) * ' ' + 82 * '-' + '>')
    while (is_sequence_decreasing and from_x >= to_x) or\
            (not is_sequence_decreasing and from_x <= to_x):

        y1_cur_value = y1(from_x)
        am_of_left_spaces = int(((int(dials_precision[1:index]) + 2) - \
                                 len(dials_precision % from_x)) / 2)
        am_of_right_spaces = am_of_left_spaces
        max_y1_value_difference = (max_y1_value - min_y1_value) +\
                                  (max_y1_value == min_y1_value)
        cur_y1_value_and_min_difference = (y1_cur_value - min_y1_value) +\
                                          (y1_cur_value == min_y1_value) *\
                                          ((max_y1_value == min_y1_value))
        pos_of_x = int(cur_y1_value_and_min_difference * 80 /\
                       max_y1_value_difference)
        ratio = max_y1_value_difference / 80
        axis_x_pos = abs(int((- min_y1_value) * 80 / max_y1_value_difference))
        if (axis_x_pos > 80):
            axis_x_pos = 81

        print(am_of_left_spaces * ' ' + dials_precision % from_x +\
              am_of_right_spaces * ' ', end='')

        if (negative_value_exists):
            if y1_cur_value <= 0 - ratio / 2:
                req_aux = axis_x_pos - pos_of_x
                if (req_aux != 0):
                    print(pos_of_x*' ' + '*' + (req_aux - 1)*' ' + '|')
                else:
                    print((axis_x_pos- 1)*' ' + '*' + '|')
            elif y1_cur_value >= 0 + ratio / 2:
                req_aux = pos_of_x - axis_x_pos
                if (req_aux != 0):
                    print(axis_x_pos * ' ' + '|' + (req_aux - 1) * ' ' + '*')
                else:
                    print((axis_x_pos)*' ' + '|*')
            else:
                print(axis_x_pos*' ' + '*')
        else:
            print('|' + pos_of_x*' ' + '*')
            axis_x_pos = 0

        from_x += pace_x

    print((int(dials_precision[1:index]) + 2 + axis_x_pos) * ' ' + '|\n' + \
          (int(dials_precision[1:index]) + axis_x_pos) * ' ' + 'x V')
else:
    print("Incorrect input.")
