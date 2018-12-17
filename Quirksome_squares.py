from math import sqrt, floor
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

def long_multiply(dial_len):
    digit_length = int(input())
    max_dial = [int(int(digit_length / 2) * '9'), int(int(digit_length / 2) * '9')]
    cur_dial = [0, 0]
    while cur_dial[0] <= max_dial[0]:
        square = str(cur_dial[0] + cur_dial[1])
        result = [0 for i in range(len(square) * 2)]
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
        if len(result) > int(digit_length / 2):
            left_half = int(''.join(result[:int(-digit_length / 2)]))
            right_half = int(''.join(result[int(-digit_length / 2):]))
        else:
            right_half = int(''.join(result))
            left_half = 0

        if left_half == cur_dial[0] and right_half == cur_dial[1]:
            left_half = str(left_half)
            right_half = str(right_half)
            while len(left_half) < int(digit_length / 2):
                left_half = '0' + left_half
            while len(right_half) < int(digit_length / 2):
                right_half = '0' + right_half
            print(left_half + right_half)

        cur_dial[1] += 1
        cur_dial[0] += cur_dial[1] // 10 ** int(digit_length / 2)
        cur_dial[1] %= 10 ** int(digit_length / 2)

for digit_length in input_file:
    try:
        int_digit_length = int(digit_length)
        half, maximum = int(int_digit_length / 2), int(int_digit_length * '9')
        for i in range(maximum + 1):
            root = sqrt(i)
            if root - floor(root) == 0:
                i_string, left_half, right_half = str(i), 0, 0
                i_length = len(i_string)
                if i_length > int_digit_length / 2:
                    right_half = int(i_string[-half:])
                    left_half = int(i_string[:-half])
                else:
                    right_half = i
                    left_half = 0

                if (right_half + left_half)**2 == i:
                    dial = (half - len(str(left_half))) * '0' + str(left_half)
                    dial += (half - len(str(right_half))) * '0' + str(right_half)
                    output_file.write(dial + '\n')
    except ValueError:
        print("Incorrect input")
output_file.close()
input_file.close()
