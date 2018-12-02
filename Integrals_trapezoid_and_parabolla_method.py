from math import cos

def trap_met(from_x, cur_section_number, section_length):
    prev_field_area = from_x + (cur_section_number - 1)*section_length
    return (cos(prev_field_area) + cos(prev_field_area +
                                       section_length))*section_length / 2

def parab_met(x, cur_section_number, is_even, section_len):
    return (is_even*4 + (not is_even)*2)*cos(x + cur_section_number*section_len)

def calculate(from_x, to_x, n, parab_count=True, trap_count=True):
    integral = [0, 0, 0]
    section_len = abs(from_x - to_x) / n
    is_even = False  # используется для определения, является ли номер текущего отрезка четным
    # нужно для вычислений методом парабол
    for cur_section_number in range(1, n):  # текущий номер отрезка
        if trap_count:
            integral[0] += trap_met(from_x, cur_section_number, section_len)
        if parab_count and cur_section_number != n - 1:
            integral[1] += parab_met(from_x, cur_section_number, is_even,
                                     section_len)
        is_even = not is_even
    integral[-1] = section_len
    return integral

def Menu():
    try:
        AMOUNT_OF_SIGNS = 16
        TEXT_FORMAT = "{0:^{1}}"
        DIAL_FORMAT = "{0:^{1}.9g}"
        sections = [0, 0, 4, 2]
        '''В пячейках хранятся числа, обозначающие
           количество отрезков, на которые надо разделить областьъ
           под графиком. В первых двух - вводимые n1, n2.
           Во вторых двух - последние количества отрезков
           при вычислении интеграла с заданной точностью'''
        from_x, to_x, sections[0], sections[1], eps = map(float,
                                                          input(
                                                              "Enter x's beginning and ending coordinates, two dials, describing\n"
                                                              "an amount of fields graphic should be divided to during\n"
                                                              "calculating, and the precious of calculating. All in one line,\n"
                                                              "dividing them by space. :").split())
        integral = [0, 0, cos(from_x) + cos(to_x), cos(from_x) + cos(to_x), 0,
                    0, 0, 0]
        '''в первых двух ячеках вычисления методом трапеций
           при разбиении на первое и второе количество
           отрезков соответственно, две вторые - методом парабол,
           последние две хранят значения, получившиеся в результате
           вычисления интеграла с заданной точностью'''
        for cur_amount_of_sections in range(
                2):  # отвечает за количество отрезков (0 - n1, 1 - n2)
            aux = calculate(from_x, to_x, int(sections[cur_amount_of_sections]))
            integral[cur_amount_of_sections], integral[
                cur_amount_of_sections + 2] = \
                aux[0], aux[1] + integral[cur_amount_of_sections + 2]
            integral[2 + cur_amount_of_sections] *= abs(from_x - to_x) / \
                                                    (3 * int(sections[
                                                                 cur_amount_of_sections]))

        print('|', TEXT_FORMAT.format('method', AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(sections[0], AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(sections[1], AMOUNT_OF_SIGNS), '|', sep='|')
        print((AMOUNT_OF_SIGNS + 2) * 3 * '-')
        print('|', TEXT_FORMAT.format('trapezoid', AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(integral[0], AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(integral[1], AMOUNT_OF_SIGNS), '|',
              sep='|')
        print((AMOUNT_OF_SIGNS + 2) * 3 * '-')
        print('|', TEXT_FORMAT.format('parabola', AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(integral[2], AMOUNT_OF_SIGNS),
              DIAL_FORMAT.format(integral[3], AMOUNT_OF_SIGNS), '|',
              sep='|')
        print((AMOUNT_OF_SIGNS + 2) * 3 * '-')

        # вычисиления с заданной точностью
        cur_trap_and_parab = calculate(from_x, to_x, sections[-1])
        cur_trap_and_parab[1] += cos(from_x) + cos(to_x)
        cur_trap_and_parab[1] *= cur_trap_and_parab[-1] / 3
        integral[5], integral[7] = cur_trap_and_parab[0], cur_trap_and_parab[1]

        cur_trap_and_parab = calculate(from_x, to_x, sections[-2])
        cur_trap_and_parab[1] += cos(from_x) + cos(to_x)
        cur_trap_and_parab[1] *= cur_trap_and_parab[-1] / 3
        integral[4], integral[6] = cur_trap_and_parab[0], cur_trap_and_parab[1]

        parab, trap = True, True
        if (abs(integral[4] - integral[5])) <= eps: trap = False
        if (abs(integral[6] - integral[7])) <= eps: parab = False

        while parab or trap:
            integral[5], integral[7] = integral[4], integral[6]
            sections[2], sections[3] = sections[2] * 2, sections[2]

            cur_trap_and_parab = calculate(from_x, to_x, int(sections[2]),
                                           parab, trap)
            if trap:
                integral[4] = cur_trap_and_parab[0]
            if parab:
                cur_trap_and_parab[1] += cos(from_x) + cos(to_x)
                cur_trap_and_parab[1] *= cur_trap_and_parab[-1] / 3
                integral[6] = cur_trap_and_parab[1]

            if (abs(integral[4] - integral[5])) <= eps: trap = False
            if (abs(integral[6] - integral[7])) <= eps: parab = False

        print(
            "Integral's value calculated by trapezoid method with entered precious:",
            DIAL_FORMAT.format(integral[4], AMOUNT_OF_SIGNS))
        print(
            "Integral's value calculated by trapezoid method with entered precious:",
            DIAL_FORMAT.format(integral[6], AMOUNT_OF_SIGNS), end='\n\n')
        trap0_abs, parab0_abs = abs(integral[4] - integral[0]), abs(
            integral[6] - integral[2])
        trap1_abs, parab1_abs = abs(integral[4] - integral[1]), abs(
            integral[6] - integral[3])
        print("Absolute mistake (trapezoid method).\nOn", int(sections[0]),
              "fields divided:",
              DIAL_FORMAT.format(trap0_abs, AMOUNT_OF_SIGNS))
        print('On', int(sections[1]), "fields divided:",
              DIAL_FORMAT.format(trap1_abs, AMOUNT_OF_SIGNS),
              end='\n\n')
        print("Absolute mistake (parabola method).\nOn", int(sections[0]),
              "fields divided:",
              DIAL_FORMAT.format(parab0_abs, AMOUNT_OF_SIGNS))
        print('On', int(sections[1]), "fields divided:",
              DIAL_FORMAT.format(parab1_abs, AMOUNT_OF_SIGNS),
              end='\n\n')
        print("Relative mistake (trapezoid method).\nOn", int(sections[0]),
              "fields divided:",
              DIAL_FORMAT.format(trap0_abs / integral[4], AMOUNT_OF_SIGNS))
        print('On', int(sections[1]), "fields divided:",
              DIAL_FORMAT.format(trap1_abs / integral[4], AMOUNT_OF_SIGNS),
              end='\n\n')
        print("Relative mistake (parabola method).\nOn", int(sections[0]),
              "fields divided:",
              DIAL_FORMAT.format(parab0_abs / integral[6], AMOUNT_OF_SIGNS))
        print('On', int(sections[1]), "fields divided:",
              DIAL_FORMAT.format(parab1_abs / integral[6], AMOUNT_OF_SIGNS),
              end='\n\n')
    except ValueError:
        print("Incorrect input!")
    except ...:
        print("Mistake during program running.")
Menu()
