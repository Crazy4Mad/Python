#Шевцов Егор
from math import sqrt,ceil

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
prec = "%10.6g" #точность числа
ind = prec.find('.') #получаю позицию '.', чтобы потом считать целую часть от числа после%
aux, length = int(int(prec[1:ind]) / 2), (int(prec[1:ind]) + 2) * 4 + 5
l_mul, r_mul, delim =  int(aux + (aux*2 < int(prec[1]))), aux, ' '
is_dec = to_x - from_x < 0

if (pace_x != 0) and (to_x - from_x)*pace_x >= 0:
    min_val, max_val, x_copy = y1(from_x), y1(from_x), from_x
    negative_exists = False
    #специльным образом отформатированный вывод всех значений в строку
    print("|" + (l_mul + 1)*delim + 'x' + r_mul*delim + '|' + l_mul*delim +\
          "y1" + r_mul*delim + '|' + l_mul*delim + 'y2' + r_mul*delim + '|'\
          + l_mul*delim + "y3" + r_mul*delim + "|\n" + length * '-')

    while(is_dec and x_copy >= to_x) or (not is_dec and x_copy <= to_x):
        y1_val = y1(x_copy)
        min_val = (min_val > y1_val)*y1_val + (min_val <= y1_val)*min_val
        max_val = (max_val < y1_val)*y1_val + (max_val >= y1_val)*max_val
        negative_exists += y1_val < 0
        print('|' + delim + prec%x_copy + delim + '|' + delim\
              +prec%y1_val+ delim + '|', end='')
        if (x_copy != 0):
            print(delim + prec%y2(x_copy) + delim + '|' + delim\
                  + prec%y3(x_copy) + delim + "|\n" + length*'-')
        else:
            print((l_mul - 2) * delim + "не сущ" + (r_mul - 2)*delim + '|'\
                  + (l_mul - 2)*delim + "не сущ" + (r_mul - 2)*delim + "|\n"\
                  + length * '-')
        x_copy += pace_x

    #график
    print('\n\n','\t\t', "График функции y1 = x**3 - 2*x**2 + 4*x - 8", '\n')
    print((int(prec[1:ind]) + 2) * ' ' + 82*' ' + 'y')
    print((int(prec[1:ind]) + 2) * ' ' + 82*'-' + '>')
    while (is_dec and from_x >= to_x) or (not is_dec and from_x <= to_x):
        y1_val = y1(from_x)
        l_s = int(((int(prec[1:ind]) + 2) - len(prec%from_x)) / 2)
        r_s = l_s
        m_dif = (max_val - min_val) + (max_val == min_val)
        dif = (y1_val - min_val) + (y1_val == min_val)*((max_val == min_val))
        pos_of_x = int(dif * 80 / m_dif)
        axis_x_pos = abs(int((- min_val) * 80 / m_dif))
        ratio = m_dif / 80

        print(l_s*' ' + prec%from_x + r_s*' ', end='')
        if (negative_exists):
            if y1_val < 0 - ratio:
                req_aux = axis_x_pos - pos_of_x
                print(pos_of_x*' ' + '*' + (req_aux - 1)*' ' + '|')
            elif y1_val > 0 + ratio:
                req_aux = pos_of_x - axis_x_pos
                print(axis_x_pos*' ' + '|' + (req_aux - 1)*' ' + '*')
            else:
                print(pos_of_x*' ' + '*')
        else:
            print('|' + pos_of_x*' ' + '*')
            axis_x_pos = 0
        from_x += pace_x
    print((int(prec[1:ind]) + 2 + axis_x_pos) * ' ' + '|\n' + \
          (int(prec[1:ind]) + axis_x_pos) * ' ' + 'x V')
else:
    print("Incorrect input.")
