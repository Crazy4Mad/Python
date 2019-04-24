from math import sin, cos, pi

def function(x):
    return sin(x)

def proizvodnaya(x):
    return cos(x)
def new_x_find(prev, prev_prev):
    return prev - (prev - prev_prev)*function(prev) / (function(prev) - function(prev_prev))

def find_root(from_x, to_x, bias, max_iters):
    if abs(to_x - from_x) >= 2*pi:
        return "More than one root"
    cur_x, prev_x, prev_prev = new_x_find(from_x, to_x), from_x, to_x
    iters = 1
    while abs(cur_x - prev_x) > bias and iters <= max_iters:
        prev_x, prev_prev = cur_x, prev_x
        cur_x = new_x_find(prev_x, prev_prev)
        iters += 1
    if (cur_x + pi <= to_x or cur_x - pi >= from_x)\
            and cur_x <= to_x and cur_x >= from_x:
        cur_x = "More than one root"
    elif cur_x > to_x or cur_x < from_x:
        cur_x = "No roots or more than one"
    if iters > max_iters:
        cur_x = "Max amount of operations exceeded"
    return [cur_x, iters]

def roots(a, b, max_iters, pace, bias):
    amount_of_roots = 0
    FORMAT="{:^.3f}"
    while a < b:
        root = find_root(a, min(a + pace, b), bias, max_iters)
        try:
            print(amount_of_roots + 1, '[' + FORMAT.format(a) + ';' +
              FORMAT.format(min(a + pace, b)) + ']',
              FORMAT.format(float(root[0])),
              FORMAT.format(function(float(root[0]))),
              root[1], '-', sep='\t')
            amount_of_roots += 1
        except ValueError:
            print(amount_of_roots + 1, '[' + FORMAT.format(a) + ';' +
                  FORMAT.format(min(a + pace, b)) + ']',
                  '-', '-', '-', root[0], sep='\t')
        a += pace
roots(14, 30, 90, 3*pi/2, 10**(-3))