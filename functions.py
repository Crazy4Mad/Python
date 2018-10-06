from math import sqrt

def y1(x):
    return x**3 - 2*x**2 + 4*x - 8

def y2(x):
    #сделать проверку на x, равен ли он 0
    return 1 - 1/x**2

def y3(x):
    return sqrt(abs(y1(x)*y2(x)))

from_x, to_x, pace_x = map(float, input("Enter the first and the last"\
                        " x-coordinates and a pace dividing them by a"\
                                        " space:").split())

#переменные для динамического вычисления отступов, границ, значений в табличке
prec, mul = "%10.6g", 4
ind = prec.find('.')
aux, length = int(int(prec[1:ind]) / 2), (int(prec[1:ind]) + 2) * 4 + 5
l_mul, r_mul, delim =  int(aux + (aux*2 < int(prec[1]))), aux, ' '
is_dec = to_x - from_x < 0

if (pace_x != 0) and (to_x - from_x)*pace_x >= 0:
    min_val, max_val, x_copy = y1(from_x), y1(from_x), from_x
    #специльным образом отформатированный вывод всех значений в строку
    print("|" + (l_mul + 1)*delim + 'x' + r_mul*delim + '|' + l_mul*delim +\
          "y1" + r_mul*delim + '|' + l_mul*delim + 'y2' + r_mul*delim + '|'\
          + l_mul*delim + "y3" + r_mul*delim + "|\n" + length * '-')

    while(is_dec and x_copy >= to_x) or (not is_dec and x_copy <= to_x):
        print('|' + delim + prec%x_copy + delim + '|' + delim\
              +prec%y1(x_copy)+ delim + '|', end='')
        if (x_copy != 0):
            print(delim + prec%y2(x_copy) + delim + '|' + delim\
                  + prec%y3(x_copy) + delim + "|\n" + length*'-')
        else:
            print((l_mul - 2) * delim + "не сущ" + (r_mul - 2)*delim + '|'\
                  + (l_mul - 2)*delim + "не сущ" + (r_mul - 2)*delim + "|\n"\
                  + length * '-')
        x_copy += pace_x

else:
    print("Incorrect input.")
