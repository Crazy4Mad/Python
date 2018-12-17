square = input("Enter a dial:")
result = [0 for i in range(len(square)*2)]
cur_multiply = [0 for i in range(len(square) + 1)]
square = [int(x) for x in square]
aux = -1
for multiply_on in square[::-1]:
    cur_multiply[-len(square):] = square
    add = 0
    for j in range(len(cur_multiply) - 1, 0, -1):
        cur_multiply[j] *= multiply_on
        cur_multiply[j] += add
        add = cur_multiply[j] // 10
        cur_multiply[j] %= 10
    cur_multiply[0] += add

    if cur_multiply[0] == 0:
        cur_multiply.pop(0)
    mult = -1
    for i in range(aux, aux - len(cur_multiply), -1):
        result[i] += cur_multiply[mult]
        mult -= 1
    cur_multiply = [0 for i in range(len(square) + 1)]
    aux -= 1

for i in range(len(result) - 1, 0, -1):
    result[i - 1] += result[i] // 10
    result[i] %= 10

result = [str(x) for x in result]
print(''.join(result))
