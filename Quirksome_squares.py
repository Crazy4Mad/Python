from math import sqrt, floor
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

def long_multiply(dial_len):
    pass

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
