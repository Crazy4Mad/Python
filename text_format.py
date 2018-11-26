def TO_ORIGINAL(strings_width, cur_pos, max_width):
    if cur_pos == 'r':
        for i in range(len(Mass)):
            Mass[i] = Mass[i][max_width - strings_width[i]:]
    elif cur_pos == 'l':
        for i in range(len(Mass)):
            Mass[i] = Mass[i][:strings_width[i]]
    else:
        for i in range(len(Mass)):
            half = int((max_width - strings_width[i]) / 2)
            Mass[i] = Mass[i][half:max_width - half + 1]

def align_left(strings_width, cur_pos, max_width):
    if cur_pos != '' and cur_pos != 'l':
        TO_ORIGINAL(strings_width, cur_pos, max_width)
    for i in range(len(Mass)):
        if cur_pos != 'l':
            Mass[i] = Mass[i] + (max_width - len(Mass[i])) * ' '
        print(Mass[i])
    cur_pos = 'l'
    Menu(strings_width, cur_pos)

def align_center(strings_width, cur_pos, max_width):
    if cur_pos != '' and cur_pos != 'c':
        TO_ORIGINAL(strings_width, cur_pos, max_width)
    for i in range(len(Mass)):
        if cur_pos != 'c':
            half = int((max_width - strings_width[i]) / 2)
            Mass[i] = half *' ' + Mass[i] + (max_width - strings_width[i] - half)*' '
        print(Mass[i])
    cur_pos = 'c'
    Menu(strings_width, cur_pos)

def align_right(strings_width, cur_pos, max_width):
    if cur_pos != '' and cur_pos != 'r':
        TO_ORIGINAL(strings_width, cur_pos, max_width)
    for i in range(len(Mass)):
        if cur_pos != 'r':
            Mass[i] = (max_width - strings_width[i])*' ' + Mass[i]
        print(Mass[i])
    cur_pos = 'r'
    Menu(strings_width, cur_pos)
    
def change_word(strings_width, cur_pos, max_width, is_remove = False):
    if not is_remove:
        before = input("What word do you want to change?\n")
        after = input("What word do you want to change on?\n")
    else:
        before = input("What word do you want to remove?\n")
        after = ''
    if cur_pos != '':
        TO_ORIGINAL(strings_width, cur_pos, max_width)
    for i in range(len(Mass)):
        aux = Mass[i].split(before)
        new_i_mass = aux[0]
        for j in range(1, len(aux)):
            right, left = True, True
            if (len(aux[j - 1]) >= 1 and aux[j - 1][-1] != ' ') or\
                    (len(aux[j - 1]) == 0 and j != 1):
                left = False
            if (left and len(aux[j]) >= 1 and aux[j][0] != ' ') or\
                    (len(aux[j]) == 0 and j != len(aux) - 1):
                right = False
            if right and left:
                new_i_mass += after
            else:
                new_i_mass += before
            new_i_mass += aux[j]
            if is_remove and right and left and len(aux[j]) >= 1 and aux[j][0] == ' ':
                new_i_mass = new_i_mass[:-len(aux[j])] + \
                             (-len(aux[j]) < -1)*new_i_mass[-len(aux[j]) + 1:]
        while is_remove and len(new_i_mass) > 0 and new_i_mass[-1] == ' ':
            new_i_mass = new_i_mass[:-1]
        Mass[i] = new_i_mass
        strings_width[i] = len(Mass[i])
        if max_width < strings_width[i]:
            max_width = strings_width[i]
    print()
    for i in range(len(Mass)):
        print(Mass[i])
    Menu(strings_width, cur_pos)

def remove_word(strings_width, cur_pos, max_width):
    change_word(strings_width, cur_pos, max_width, True)

def ariphmetics(strings_width):
    pass

def Menu(strings_width, cur_pos):
    print("\nWhat do you want to do with text?")
    switch_case_emulator = {1: align_left,
                            2: align_center,
                            3: align_right,
                            4: change_word,
                            5: remove_word,
                            6: ariphmetics}
    print("1-Align it left", "2-Align it center", "3-Align it right",
          "4-Change a word", "5-Remove a word", "6-Ariphmetics", sep='\n')
    answer = int(input())
    while answer not in switch_case_emulator:
        print("Incorrect dial was entered. Try again.")
        answer = int(input())
    flag = answer <= 3
    switch_case_emulator[answer](strings_width, cur_pos, max(strings_width))

try:
    Mass = []
    amount_of_strings = int(input("Enter an amount of strings:"))
    width = [0 for i in range(amount_of_strings)]
    print(width)
    for i in range(amount_of_strings):
        Mass.append(input())
        width[i] = (len(Mass[i]))
    cur_pos = ''
    Menu(width, cur_pos)
except ValueError:
    print("Incorrect input")
