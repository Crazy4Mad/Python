from math import sin, pi

def function(x):
    return sin(x)

def new_x_find(prev, prev_prev):
    return prev - ((prev - prev_prev) / (function(prev) - function(prev_prev))*function(prev))

def find_root(from_x, to_x, bias, max_iters):
    if to_x - from_x >= 2*pi:
        return "More than one root"
    cur_x, prev_x, prev_prev = new_x_find(from_x, to_x), from_x, to_x
    iters = 1
    flag = True
    while function(cur_x) > bias and iters <= max_iters and cur_x <= to_x and cur_x >= from_x:
        prev_x, prev_prev = cur_x, prev_x
        cur_x = new_x_find(prev_x, prev_prev)
        iters += 1
    if cur_x + pi <= to_x or cur_x - pi >= from_x:
        flag = False
    if flag:
        if iters > max_iters:
            return "Max amount of operations exceeded"
        elif cur_x > to_x or cur_x < from_x:
            return "No roots"
        else:
            return [cur_x, iters]
    else:
        return "More than one root"
print(find_root(-3, -1, 0.001, 9))