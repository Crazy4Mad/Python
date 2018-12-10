from math import ceil, floor
TEXT = ["don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "than he can. Ааааааааааа-пчхи! Длина окружности",
        "не равна 3.14*5/9."]

def find_maximum(text = ["don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "than he can. Ааааааааааа-пчхи! Длина окружности",
        "не равна 3.14*5/9."]):
    max_len = 0
    for i in range(len(text)):
        max_len = max(max_len, len(text[i]))
    return max_len

def returning():
    global TEXT
    TEXT = ["don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "than he can. Ааааааааааа-пчхи! Длина окружности",
        "не равна 3.14*5/9."]

def align_left(max_len, side):
    if side != 'l':returning()
    for i in range(len(TEXT)):
        TEXT[i] += (max_len - len(TEXT[i])) * ' '
    Menu('l', max_len)

def align_right(max_len, side):
    if side != 'r':returning()
    for i in range(len(TEXT)):
        TEXT[i] = (max_len - len(TEXT[i])) * ' ' + TEXT[i]
    Menu('r', max_len)

def align_width(max_len, side):
    if side != 'w':
        returning()
        for i in range(len(TEXT)):
            spaces = max_len - len(TEXT[i])
            TEXT[i] = [j for j in TEXT[i].split(' ') if j != '']
            counter = 0
            while spaces != 0 and len(TEXT[i]) > 1:
                if counter == len(TEXT[i]) - 1:
                    counter = 0
                TEXT[i][counter] += ' '
                spaces -= 1
                counter += 1
            if len(TEXT[i]) == 1:
                TEXT[i] = floor(spaces/2)*' ' + str(TEXT[i][0]) +\
                           ceil(spaces/2)*' '
            elif len(TEXT[i]) == 0:
                TEXT[i] = spaces*' '
            else:
                TEXT[i] = ' '.join(TEXT[i])
    Menu('w', max_len)

def is_letter(before, after):
    letter_before = (before <= 'Z' and before >= 'A') or\
                    (before <= 'z' and before >= 'a') or\
                    (before <= '9' and before >= '0')
    letter_after = (after <= 'Z' and after >= 'A') or \
                    (after <= 'z' and after >= 'a') or \
                    (after <= '9' and after >= '0')
    return [letter_after, letter_after]

def replace_word(max_len, side):
    global TEXT
    word_to_replace = input("Enter a word to be replaced:")
    replace_on = input("Enter a word to replace on:")
    for j in range(len(TEXT)):
        aux = ''
        TEXT[j].split(word_to_replace)
        for i in range(1, len(TEXT[j]) - 1):
            aux += TEXT[j][i - 1]
            try:
                if is_letter(TEXT[j][i - 1][-1], TEXT[j][i + 1][0]) == [True, True]:
                    aux += replace_on
            except...:
                aux += replace_on
        TEXT[j] = aux
    Menu(find_maximum(TEXT), side)

def delete_max_length_word_in_max_len_sentence():
    returning()


def Menu(side='', max_string_len = 0):
    if TEXT != '':
        print()
        for i in range(len(TEXT)):
            print(TEXT[i])
        print()
    max_string_len = find_maximum()

    menu = {1: align_left,
            2: align_right,
            3: align_width,
            4: replace_word,
            5: delete_max_length_word_in_max_len_sentence}
    for i in range(len(menu)):
        print(i + 1, '-', ' '.join(str(menu[i + 1]).split(' ')[1].split('_')))
    answer = int(input("Enter an appropriate dial to pick up an action:"))
    while answer not in menu:
        answer = int(input("Incorrect input. Try again:"))
    menu[answer](max_string_len, side)
Menu()
