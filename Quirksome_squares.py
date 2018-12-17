from math import sqrt, floor
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for digit_length in input_file:
    try:
        int_digit_length = int(digit_length)
        for dial in range(10**int(int_digit_length / 2)):
            req_dial = dial**2
            str_req_dial = str(req_dial)
            str_req_dial = (int_digit_length - len(str_req_dial))*'0' + str_req_dial
            sum = int(str_req_dial[:int(int_digit_length / 2)]) +\
                  int(str_req_dial[int(int_digit_length / 2):])
            if dial == sum:
                output_file.write(str_req_dial + '\n')
    except ValueError:
        print("Incorrect input")
output_file.close()
input_file.close()
