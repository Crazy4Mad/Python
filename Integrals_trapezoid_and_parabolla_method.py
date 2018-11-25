from math import cos
def trapezoid_method(from_x, to_x, difference):
    return (cos(from_x) + cos(to_x))*difference / 2

def parabola_method(x, sign):
    return (sign*4 + (not sign)*2)*cos(x)

try:
    from_x, to_x, n1, n2, bias = map(float,
            input("Enter from x, to x, n1, n2 and a bias in one line:").split())
    trap_method = [0, 0]
    parab_method = [0, 0]
    difference = [abs(from_x - to_x) / n1, abs(from_x - to_x) / n2]
    amount_of_sections = [4, 2]
    trap_integrals_with_sections = [0, 0]
    parab_integrals_with_sections = [0, 0]
    cur_n = 1
    for i in range(2):
        x_copy = from_x
        sign = True
        while x_copy < to_x:
            x_copy += difference[i]
            parab_method[i] += parabola_method(x_copy, sign)
            trap_method[i] += trapezoid_method(x_copy, x_copy - difference[i],
                                           difference[i])
            sign = not sign
        parab_method[i] += cos(from_x) + cos(to_x) - parabola_method(x_copy, not sign)
        parab_method[i] *= difference[i] / 3

    #parabola method
    difference = [abs(from_x - to_x) / amount_of_sections[0],
              abs(from_x - to_x) / amount_of_sections[1]]
    for i in range(2):
        x_copy = from_x
        sign = True
        while x_copy < to_x:
            x_copy += difference[i]
            parab_integrals_with_sections[i] += parabola_method(x_copy, sign)
            sign = not sign
        parab_integrals_with_sections[i] += cos(from_x) + cos(to_x) -\
                                        parabola_method(x_copy, not sign)
        parab_integrals_with_sections[i] *= difference[i] / 3

    while abs(parab_integrals_with_sections[0] - parab_integrals_with_sections[1]) > bias:
        amount_of_sections[0], amount_of_sections[1] = amount_of_sections[0]*2,\
                                                   amount_of_sections[0]
        parab_integrals_with_sections[0], parab_integrals_with_sections[1] = 0,\
                                      parab_integrals_with_sections[0]
        difference[0], difference[1] = abs(from_x - to_x) / amount_of_sections[0],\
                                   difference[0]
        x_copy = from_x
        sign = True
        while x_copy < to_x:
            x_copy += difference[0]
            parab_integrals_with_sections[0] += parabola_method(x_copy, sign)
            sign = not sign
        parab_integrals_with_sections[0] += cos(from_x) + cos(to_x) -\
                                        parabola_method(x_copy, not sign)
        parab_integrals_with_sections[0] *= difference[0] / 3

    #trapezoid method
    amount_of_sections = [4, 2]
    difference = [abs(from_x - to_x) / amount_of_sections[0],
              abs(from_x - to_x) / amount_of_sections[1]]
    for i in range(2):
        x_copy = from_x
        sign = True
        while x_copy < to_x:
            x_copy += difference[i]
            trap_integrals_with_sections[i] += trapezoid_method(x_copy,
                                        x_copy - difference[i], difference[i])
            sign = not sign

    while abs(trap_integrals_with_sections[0] - trap_integrals_with_sections[1]) > bias:
        amount_of_sections[0], amount_of_sections[1] = amount_of_sections[0]*2,\
                                                   amount_of_sections[0]
        trap_integrals_with_sections[0], trap_integrals_with_sections[1] = 0,\
                                        trap_integrals_with_sections[0]
        difference[0], difference[1] = abs(from_x - to_x) / amount_of_sections[0],\
                                   difference[0]
        x_copy = from_x
        sign = True
        while x_copy < to_x:
            x_copy += difference[0]
            trap_integrals_with_sections[0] += trapezoid_method(x_copy,
                                        x_copy - difference[0], difference[0])
            sign = not sign

    print('', "{:^16}".format('method'), "{:^16.10g}".format(n1),
      "{:^16.10g}".format(n2), '', sep=' | ')
    print('', (16*3 + 3*4 - 2)*'-')
    print('', "{:^16}".format('trapezoid'), "{:^16.10g}".format(trap_method[0]),
      "{:^16.10g}".format(trap_method[1]), '', sep=' | ')
    print('', (16*3 + 3*4 - 2)*'-')
    print('', "{:^16}".format('parabol'), "{:^16.10g}".format(parab_method[0]),
      "{:^16.10g}".format(parab_method[1]), '', sep=' | ')
    print('', (16*3 + 3*4 - 2)*'-')

    print("Trapezoid method (with e precious):", trap_integrals_with_sections[0])
    print("Parabola method (with e precious):", trap_integrals_with_sections[1])
except ValueError:
    print("Incorrect input")
