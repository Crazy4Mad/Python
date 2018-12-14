def NOD(first, second):
    minimum = min(first, second)
    nod = 1
    for i in range(1, minimum + 1):
        if first % i == 0 and second % i == 0:
            nod = i
    return nod


dial = str(float(input("Введите вещественное число:"))).split('.')
after_dot = int(dial[1])
if after_dot != 0:
    a, b = int(dial[1]), 10**len(str(dial[1]))
    if b == 0:
        b = 1
    nod = NOD(a, b)
    a, b = int(a / nod), int(b / nod)
    length = max(len(str(a)), len(str(b)))
    print((len(dial[0]) + 1)*' ' + "{0:^{1}g}".format(a, length))
    print(dial[0] + ' ' + '-'*length)
    print((len(dial[0]) + 1)*' ' + "{0:^{1}g}".format(b, length))
else:
    print(dial[0])
