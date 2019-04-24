from math import sin, cos, pi

def function(x):
    return sin(x)

def new_x_find(prev, prev_prev):
    return prev - (prev - prev_prev)*function(prev) / (function(prev) - function(prev_prev))

def find_root(from_x, to_x, bias, max_iters):
    cur_x, prev_x, prev_prev = new_x_find(from_x, to_x), from_x, to_x
    iters = 1
    while abs(function(cur_x)) > bias and iters <= max_iters:
        prev_x, prev_prev = cur_x, prev_x
        cur_x = new_x_find(prev_x, prev_prev)
        iters += 1
    while cur_x < from_x:
        cur_x += pi
    if iters > max_iters:
        cur_x = "Max amount of operations exceeded"
    return [cur_x, iters]

def aux(from_x, to_x, bias, max_iters):
    res = function(from_x)*function(to_x)
    if res <= 0:
        if to_x - from_x < 2*pi:
            pace = (to_x - from_x) / 10**4
            changes = 0
            for i in range(10**4):
                if function(from_x + i*pace)*function(from_x + (i + 1)*pace) < 0:
                    changes += 1
                elif i != 0 and i != 10**4 - 1 and\
                        function(from_x + i*pace)*function(from_x + (i + 1)*pace) == 0:
                    if function(from_x + (i - 1)*pace)*function(from_x + (i + 2)*pace) < 0:
                        changes += 1
                if changes >= 2 and not(res == 0 and changes <= 1):
                    return ["More than one root"]
            return find_root(from_x, to_x, bias, max_iters)
        else:
            return ["More than one root"]
    else:
        pace = (to_x - from_x) / 10 ** 4
        changes = 0
        for i in range(10 ** 4):
            if function(from_x + i * pace) * function(
                    from_x + (i + 1) * pace) < 0:
                return ["More than one root"]
            elif i != 0 and i != 10 ** 4 - 1 and \
                    function(from_x + i * pace) * function(
                from_x + (i + 1) * pace) == 0:
                if function(from_x + (i - 1) * pace) * function(
                        from_x + (i + 2) * pace) < 0:
                    return ["More than one root"]
        return ["No roots"]



def roots(a, b, max_iters, pace, bias):
    amount_of_roots = 0
    FORMAT="{:^.3f}"
    while a < b:
        root = aux(a, min(a + pace, b), bias, max_iters)
        try:
            print(amount_of_roots + 1, '[' + FORMAT.format(a) + ';' +
              FORMAT.format(min(a + pace, b)) + ']',
              FORMAT.format(float(root[0])),
              FORMAT.format(function(float(root[0]))),
              root[1], '-', sep='\t')
            amount_of_roots += 1
        except ValueError:
            print('-', '[' + FORMAT.format(a) + ';' +
                  FORMAT.format(min(a + pace, b)) + ']',
                  '-', '-', '-', root[0], sep='\t')
        a += pace
roots(-3, 1, 90, 5*pi/120, 10**(-3))