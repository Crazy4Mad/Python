from math import ceil, floor
from copy import deepcopy
TEXT = ["than he can. пчхи-Ааааааааааа! Длина окружности",
        "don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "не равна 5 +3 +a +15"]
text_copy = deepcopy(TEXT)
strings_width = [0 for i in range(len(TEXT))]

def find_maximum():
    global text_copy
    max_len = 0
    for i in range(len(text_copy)):
        strings_width[i] = len(text_copy[i])
        max_len = max(max_len, len(text_copy[i]))
    return max_len

def RETURNING():
    global TEXT, text_copy
    TEXT = deepcopy(text_copy)


def align_left(max_len, side):
    global TEXT
    if side != 'l':
        RETURNING()
        for i in range(len(TEXT)):
            TEXT[i] += (max_len - len(TEXT[i])) * ' '
    Menu('l', max_len)

def align_right(max_len, side):
    global TEXT
    if side != 'r':
        RETURNING()
        print(TEXT[2])
        for i in range(len(TEXT)):
            TEXT[i] = (max_len - len(TEXT[i])) * ' ' + TEXT[i]
    Menu('r', max_len)

def align_width(max_len, side):
    global TEXT
    if side != 'w':
        RETURNING()
        for i in range(len(TEXT)):
            spaces = max_len - len(TEXT[i])
            TEXT[i] = [j for j in TEXT[i].split(' ')]
            if len(TEXT[i]) == 1:
                TEXT[i] = floor(spaces/2)*' ' + str(TEXT[i][0]) +\
                           ceil(spaces/2)*' '
            elif len(TEXT[i]) == 0:
                TEXT[i] = spaces*' '
            else:
                average_spaces_per_word = floor(spaces / (len(TEXT[i]) - 1))
                delta = spaces - average_spaces_per_word * (len(TEXT[i]) - 1)
                for j in range(len(TEXT[i]) - 1):
                    TEXT[i][j] += " " * average_spaces_per_word
                    if delta > 0:
                        TEXT[i][j] += ' '
                        delta -= 1
                TEXT[i] = ' '.join(TEXT[i])
    Menu('w', max_len)

def is_letter(before, after, prev = 'A'):
    # флаги, отвечающие за пустые символы слева и справа от слова
    aux1, aux2 = False, False
    if before != '':
        #предыдущий символ не является буквой или дефисом
        letter_before = (before[-1] <= 'Z' and before[-1] >= 'A') or\
                    (before[-1] <= 'z' and before[-1] >= 'a') or\
                        (before[-1] <= 'Я' and before[-1] >= 'А') or \
                    (before[-1] <= 'я' and before[-1] >= 'а') or\
                    before[-1] == '-'
    else:
        letter_before = False
        aux1 = True
    if after != '':
        letter_after = (after[0] <= 'Z' and after[0] >= 'A') or\
                    (after[0] <= 'z' and after[0] >= 'a') or\
                        (after[0] <= 'Я' and after[0] >= 'А') or \
                    (after[0] <= 'я' and after[0] >= 'а') or\
                    after[0] == '-'
    else:
        letter_after = False
        aux2 = True
    return [letter_before, letter_after or prev == '', aux1 and aux2]

def replace_word(max_len, side, delete = False):
    global TEXT, text_copy
    RETURNING()
    if not delete:
        word_to_replace = input("Enter a word to be replaced:")
        replace_on = input("Enter a word to replace on:")
    else:
        word_to_replace = input("Enter a word to be deleted:")
        replace_on = ''
    for j in range(len(TEXT)):
        #делю строку на слова
        TEXT[j] = TEXT[j].split()
        for k in range(len(TEXT[j])):
            #делю слово на нужное мне подслово
            TEXT[j][k] = TEXT[j][k].split(word_to_replace)
            # сюда записываю измененную строку
            new_text = TEXT[j][k][0]
            for m in range(1, len(TEXT[j][k])):
                #проверяю значение элемента перед предыдущим для того, чтобы понять
                #присутствуют ли в слове несколько нужных подслов подряд или нет
                if m >= 2:#если этот элемент есть
                    result = is_letter(TEXT[j][k][m - 1], TEXT[j][k][m],
                                       TEXT[j][k][m - 2])
                else:
                    result = is_letter(TEXT[j][k][m - 1], TEXT[j][k][m])

                #если предыдущий символ не буква, последующий символ тоже не буква,
                #и заменяемое слово не является подсловом в слове или же если заменяемое
                #слово не ограничено ни до, ни после никакими символами, то заменяем слово
                if result == [False, False, False] or\
                        (result == [False, False, True] and m - 1 == 0 and
                        len(TEXT[j][k]) == 2):
                    if not delete:
                        new_text += replace_on + TEXT[j][k][m]
                    else:
                        new_text += TEXT[j][k][m]
                else:
                    new_text += word_to_replace + TEXT[j][k][m]
            TEXT[j][k] = new_text
        TEXT[j] = ' '.join(TEXT[j])
    text_copy = deepcopy(TEXT)
    maximum = find_maximum()
    if side == 'r':
        align_right(maximum, '')
    elif side == 'l':
        align_left(maximum, '')
    elif side == 'w':
        align_width(maximum, '')
    Menu(side, maximum)

def delete_word(max_len, side):
    replace_word(max_len, side, True)

def delete_max_length_word_in_max_len_sentence():
    pass

def count_sums_and_difference(max_len, side):
    global TEXT, text_copy
    for i in range(len(TEXT)):
        TEXT[i] = TEXT[i].split('+')
        for j in range(len(TEXT[i])):
            TEXT[i][j] = TEXT[i][j].split(' ')
        j = 1
        while j < len(TEXT[i]):
            try:
                req_before, req_after = -1, 0
                if TEXT[i][j - 1][-1] == '':req_before = -2
                if TEXT[i][j][0] == '':req_after = 1
                first = int(TEXT[i][j - 1][req_before])
                second = int(TEXT[i][j][req_after])
                print(TEXT[i][j - 1][req_before])
                TEXT[i][j - 1][req_before] = str(first + second)
                if req_before == -2:
                    TEXT[i][j - 1].pop(-1)
                    req_before += 1
                if req_after == 1:
                    TEXT[i][j].pop(0)
                    req_after -= 1
                print(TEXT[i][j - 1])
                TEXT[i][j].pop(req_after)
                TEXT[i][j - 1].extend(TEXT[i][j])
                TEXT[i].pop(j)
                print(TEXT[i][j - 1])
            except ValueError:
                TEXT[i][j - 1] = ' '.join(TEXT[i][j - 1])
                j += 1
        TEXT[i][-1] = ' '.join(TEXT[i][-1])
        TEXT[i] = '+'.join(TEXT[i])
    text_copy = deepcopy(TEXT)
    maximum = find_maximum()
    if side == 'r':
        align_right(maximum, '')
    elif side == 'l':
        align_left(maximum, '')
    elif side == 'w':
        align_width(maximum, '')
    Menu(side, maximum)


def Menu(side='', max_string_len = 0):
    global TEXT
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
            5: delete_word,
            6: count_sums_and_difference,
            7: delete_max_length_word_in_max_len_sentence}
    for i in range(len(menu)):
        print(i + 1, '-', ' '.join(str(menu[i + 1]).split(' ')[1].split('_')))
    answer = int(input("Enter an appropriate dial to pick up an action:"))
    while answer not in menu:
        answer = int(input("Incorrect input. Try again:"))
    menu[answer](max_string_len, side)
Menu()
