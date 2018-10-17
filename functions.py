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

if (pace_x != 0) and (to_x - from_x)*pace_x >= 0 and abs(to_x - from_x):

    DIAL_LENGTH = 12
    length_of_table_lower_bound = DIAL_LENGTH * 4 + 8
    is_sequence_decreasing = to_x - from_x < 0
    min_y1_value, max_y1_value, x_copy = y1(from_x), y1(from_x), from_x
    negative_value_exists = False

    for cur_str in ['x', 'y1', 'y2', 'y3']:
        print('|' + "{1:^{0}}".format(DIAL_LENGTH, cur_str) + '|', end='')
    print('\n' + length_of_table_lower_bound*'-')


    while (is_sequence_decreasing and x_copy >= to_x) or \
            (not is_sequence_decreasing and x_copy <= to_x):
        y1_cur_value = y1(x_copy)
        min_y1_value = (min_y1_value > y1_cur_value) * y1_cur_value + \
                       (min_y1_value <= y1_cur_value) * min_y1_value
        max_y1_value = (max_y1_value < y1_cur_value) * y1_cur_value + \
                       (max_y1_value >= y1_cur_value) * max_y1_value
        negative_value_exists += y1_cur_value < 0

        for cur_val in [x_copy, y1_cur_value]:
            print('|' + "{1:^{0}.6f}".format(DIAL_LENGTH, cur_val) + '|', end='')

        if x_copy != 0:
            for cur_val in [y2(x_copy), y3(x_copy)]:
                print('|' + "{1:^{0}.6f}".format(DIAL_LENGTH, cur_val) + '|', end='')
            print()
        else:
            print(2*('|' + "{1:^{0}}".format(DIAL_LENGTH, 'не сущ.') + '|'))
        print(length_of_table_lower_bound * '-')
        x_copy += pace_x

    label = "График функции y1 = x**3 - 2*x**2 + 4*x - 8"

    print("{1:>{0}}".format(len(label) + DIAL_LENGTH, label), '\n')
    print("{aux[1]:>{aux[0]}}\n {aux[2]:>{aux[0]}}>\n".format(aux=
                [DIAL_LENGTH + 81, 'y', 82 * '-']), end='');

    MAX_Y1_VALUE_DIFFERENCE = (max_y1_value - min_y1_value) + \
                                  (max_y1_value == min_y1_value)
    RATIO = MAX_Y1_VALUE_DIFFERENCE / 80
    AXIS_X_POS = abs(int((- min_y1_value) / RATIO))
    if AXIS_X_POS > 80:
        AXIS_X_POS = 81

    while (is_sequence_decreasing and from_x >= to_x) or \
                (not is_sequence_decreasing and from_x <= to_x):

        y1_cur_value = y1(from_x)
        cur_y1_value_and_min_difference = (y1_cur_value - min_y1_value) + \
                                              (y1_cur_value == min_y1_value) * \
                                              ((max_y1_value == min_y1_value))
        pos_of_y = int(cur_y1_value_and_min_difference * 80 / \
                           MAX_Y1_VALUE_DIFFERENCE)

        print("{1:^{0}.6g}".format(DIAL_LENGTH, from_x), end='')

        if negative_value_exists:
            if y1_cur_value <= 0 - RATIO / 2:
                req_aux = AXIS_X_POS - pos_of_y
                if req_aux != 0:
                    print(pos_of_y * ' ' + '*' + (req_aux - 1) * ' ' + '|')
                else:
                    print((AXIS_X_POS - 1) * ' ' + '*' + '|')
            elif y1_cur_value >= 0 + RATIO / 2:
                req_aux = pos_of_y - AXIS_X_POS
                if req_aux != 0:
                    print(AXIS_X_POS * ' ' + '|' + (req_aux - 1) * ' ' + '*')
                else:
                    print(AXIS_X_POS * ' ' + '|*')
            else:
                print(AXIS_X_POS * ' ' + '*')
        else:
            print('|' + pos_of_y * ' ' + '*')
            AXIS_X_POS = 0
        from_x += pace_x
    print((DIAL_LENGTH + AXIS_X_POS) * ' ' + '|\n',
              (DIAL_LENGTH + AXIS_X_POS - 3) * ' ' + 'x V')
else:
    print("Incorrect input")
