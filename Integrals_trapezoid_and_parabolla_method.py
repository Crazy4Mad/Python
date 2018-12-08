from math import cos, sin
def count(x, flag=True):
    return x**2*flag + x**3/3*(not flag)

def trapezoid(from_x, to_x, sections):
    delta = abs(from_x - to_x) / sections
    sum = 0
    for i in range(1, sections + 1):
        a = (count(from_x + i*delta))
        b = count(from_x + (i - 1)*delta)
        a_b_sum = (a + b)*delta / 2
        sum += a_b_sum
    return abs(sum)

def parabola(from_x, to_x, sections):
    try:
        delta = abs(from_x - to_x) / sections
        sum = 0
        sum += count(from_x) + count(to_x)
        for i in range(1, sections + 1, 2):
            sum += 4*count(from_x + i*delta)
        for i in range(2, sections, 2):
            sum += 2*count(from_x + i*delta)
        sum *= delta / 3
        return abs(sum)
    except  ZeroDivisionError: #ыскакивает при неченом количестве отрезков разбиения
        return -1

def Menu():
    try:
        DIAL_FORMAT = "{:^12.8g}"
        TEXT_FORMAT = "{:^12}"

        from_x = float(input("Enter the beginning value:"))
        to_x = float(input("Enter the ending value:"))
        first_precious = int(
            float(input("Enter the first amount of sections the function"
                        "should be divided on:")))
        sec_precious = int(
            float(input("Enter the second amount of sections the function"
                        "should be divided on:")))
        e = float(input("Enter the required precious:"))
        integral_table = [[0] * 2 for i in range(2)]

        # вычисляю интегралы с разбиением на заданные количества отрезков
        integral_table[0][0] = trapezoid(from_x, to_x, first_precious)
        integral_table[0][1] = trapezoid(from_x, to_x, sec_precious)
        integral_table[1][0] = parabola(from_x, to_x,
                                        first_precious * (first_precious
                                                          % 2 == 0))
        integral_table[1][1] = parabola(from_x, to_x,
                                        sec_precious * (sec_precious
                                                        % 2 == 0))

        print('|', TEXT_FORMAT.format('method'),
              DIAL_FORMAT.format(first_precious),
              DIAL_FORMAT.format(sec_precious), '|', sep='|')
        print(14 * 3 * '-')
        print('|', TEXT_FORMAT.format('trapezoid'),
              DIAL_FORMAT.format(integral_table[0][0]),
              DIAL_FORMAT.format(integral_table[0][1]), '|', sep='|')
        print(14 * 3 * '-')
        print('|', TEXT_FORMAT.format('parabola'),
              DIAL_FORMAT.format(integral_table[1][0]) * (
                          integral_table[1][0] != -1) +
              TEXT_FORMAT.format('-') * (integral_table[1][0] == -1),
              DIAL_FORMAT.format(integral_table[1][1]) * (
                          integral_table[1][1] != -1) +
              TEXT_FORMAT.format('-') * (integral_table[1][1] == -1),
              '|', sep='|')
        print(14 * 3 * '-')

        correct_value = abs(count(to_x, False) - count(from_x, False))
        relative_trapezoid = abs(
            max(integral_table[0]) - correct_value) / correct_value
        relative_parabola = abs(
            max(integral_table[1]) - correct_value) / correct_value

        if relative_parabola < relative_trapezoid:
            sections = 2
            cur_value = trapezoid(from_x, to_x, sections)
            while abs(cur_value - correct_value) > e:
                sections *= 2
                cur_value = trapezoid(from_x, to_x, sections)
            print("Trapezoid method with required precious:",
                  DIAL_FORMAT.format(cur_value))
            print("Amount of sections:", DIAL_FORMAT.format(sections))
        else:
            sections = 2
            cur_value = parabola(from_x, to_x, sections)
            while abs(cur_value - correct_value) > e:
                sections *= 2
                cur_value = parabola(from_x, to_x, sections)
            print("Parabola method with required precious:",
                  DIAL_FORMAT.format(cur_value))
            print("Amount of sections:", DIAL_FORMAT.format(sections))
    except ValueError:
        print("Incorrect input")
Menu()
