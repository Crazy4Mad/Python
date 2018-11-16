from math import cos
def trapezoid_method(from_x, to_x, difference):
    return (cos(from_x) + cos(to_x))*difference / 2

def parabola_method(x, sign):
    return (sign*4 + (not sign)*2)*cos(x)

from_x, to_x, n1, n2 = map(float, input("Enter from x, to x, n1, n2 in one line:").split())
trap_method = [0, 0]
parab_method = [0, 0]
difference = [abs(from_x - to_x) / n1, abs(from_x - to_x) / n2]

for i in range(2):
    x_copy = from_x
    sign = True
    while x_copy < to_x - 1e-5:
        x_copy += difference[i]
        parab_method[i] += parabola_method(x_copy, sign)
        trap_method[i] += trapezoid_method(x_copy, x_copy - difference[i], difference[i])
        sign = not sign
    parab_method[i] += cos(from_x) + cos(to_x) - parabola_method(x_copy, not sign)
    parab_method[i] *= difference[i] / 3

print(trap_method[0], parab_method[0])
print(trap_method[1], parab_method[1])
