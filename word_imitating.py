from math import ceil, floor
TEXT = ["than he can. пчхи-Ааааааааааа! Длина окружности",
        "don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "не равна 3.14*5/9."]
strings_width = [0 for i in range(len(TEXT))]

def find_maximum(text = ["than he can. Ааааааааааа-пчхи! Длина окружности",
        "don't worry, be happy now. I'm",
        "your baby tonight.", "Hello",
        "it's me. Treat your better,",
        "не равна 3.14*5/9."]):
    max_len = 0
    for i in range(len(text)):
        strings_width[i] = len(text[i])
        max_len = max(max_len, len(text[i]))
    return max_len

def RETURNING(max_len, side):
    global TEXT, strings_width
    if side == 'l':
        for i in range(len(TEXT)):
            TEXT[i] = TEXT[i][:strings_width[i]]
    elif side == 'r':
        for i in range(len(TEXT)):
            TEXT[i] = TEXT[i][max_len - strings_width[i]:]
    elif side == 'w':
        

def align_left(max_len, side):
    if side != 'l':RETURNING(max_len, side)
    for i in range(len(TEXT)):
        TEXT[i] += (max_len - len(TEXT[i])) * ' '
    Menu('l', max_len)

def align_right(max_len, side):
    if side != 'r':RETURNING(max_len, side)
    for i in range(len(TEXT)):
        TEXT[i] = (max_len - len(TEXT[i])) * ' ' + TEXT[i]
    Menu('r', max_len)

def align_width(max_len, side):
    if side != 'w':
        RETURNING(max_len, side)
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
    global TEXT
    RETURNING(max_len, side)
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
    Menu(find_maximum(TEXT), side)

def delete_word(max_len, side):
    replace_word(max_len, side, True)

def delete_max_length_word_in_max_len_sentence():
    RETURNING()


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
            5: delete_word,
            6: delete_max_length_word_in_max_len_sentence}
    for i in range(len(menu)):
        print(i + 1, '-', ' '.join(str(menu[i + 1]).split(' ')[1].split('_')))
    answer = int(input("Enter an appropriate dial to pick up an action:"))
    while answer not in menu:
        answer = int(input("Incorrect input. Try again:"))
    menu[answer](max_string_len, side)
Menu()
