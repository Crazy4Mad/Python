from math import ceil, floor
from copy import deepcopy
TEXT = ["   В конце концов партия объявит, что 25 + 2 - 0 = 5 + 7, и 7 -     ",
'5 придется в это верить. Рано или поздно она издаст такой указ, к',
'этому неизбежно ведет логика ее власти. Ее философия молчаливо ',
' отрицает не только верность твоего. 13 - 9 20 + 15 восприятия, но и само существование',
'внешнего мира. Ересь из ересей — здравый смысл. И ужасно не то, что тебя ',
' убьют за противоположное мнение, а то, что они, может быть, правы. В самом',
'деле, откуда мы знаем, что 2 - 29 = 4 + 8? Или что существует сила ',
' тяжести? Или что прошлое нельзя изменить? Если и прошлое и внешний мира',
'существуют только в сознании, а сознанием можно управлять — тогда что? ',
'        Д. Оруэлл "1984"']
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
            TEXT[i] = [j for j in TEXT[i].split()]
            length = 0
            for aux in TEXT[i]:
                a = aux
                length += len(aux)
            length += len(TEXT[i]) - 1
            spaces = max_len - length
            if len(TEXT[i]) == 1:
                TEXT[i] = floor(spaces/2)*' ' + str(TEXT[i][0]) +\
                           ceil(spaces/2)*' '
            elif len(TEXT[i]) == 0:
                TEXT[i] = spaces*' '
            else:
                j = 0
                while spaces != 0:
                    TEXT[i][j] += ' '
                    spaces -= 1
                    j += 1
                    if j > len(TEXT[i]) - 2:
                        j = 0
                TEXT[i] = ' '.join(TEXT[i])
    Menu('w', max_len)

def is_letter(before, after='', prev = 'A'):
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
            aux = TEXT[j][k]
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
            TEXT[j][k] = ' '.join(new_text.split())
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

def delete_max_length_word_in_max_len_sentence(max_len, side):
    global TEXT, text_copy
    RETURNING()
    TEXT = (' \n '.join(TEXT)).split('.')
    print(TEXT)
    for i in range(len(TEXT)):
        TEXT[i] = TEXT[i].split('!')
        for j in range(len(TEXT[i])):
            TEXT[i][j] = TEXT[i][j].split('?')

    max_len, max_f, max_s, max_t = 0, -1, -1, -1
    for i in range(len(TEXT)):
        for j in range(len(TEXT[i])):
            for k in range(len(TEXT[i][j])):
                if len(TEXT[i][j][k]) - TEXT[i][j][k].count(' \n ') > max_len:
                    max_len = len(TEXT[i][j][k])
                    max_f, max_s, max_t = i, j, k
    sentence = ''
    print(TEXT)
    if max_f != -1:
        if max_s != -1:
            if max_t != -1:
                sentence = TEXT[max_f][max_s][max_t]
            else:
                sentence = TEXT[max_f][max_s]
        else:
            sentence = TEXT[max_f]
    print(sentence)
    sentence = sentence.split(' ')

    max_word, max_ind = 0, 0
    for i in range(len(sentence)):
        if len(sentence[i]) > max_word:
            max_word = len(sentence[i])
            max_ind = i
    sentence.pop(max_ind)
    sentence = ' '.join(sentence)

    if max_f != -1:
        if max_s != -1:
            if max_t != -1:
                TEXT[max_f][max_s][max_t] = sentence
            else:
                TEXT[max_f][max_s] = sentence
        else:
            TEXT[max_f] = sentence

    for i in range(len(TEXT)):
        for j in range(len(TEXT[i])):
            if isinstance(TEXT[i][j], list):
                TEXT[i][j] = '?'.join(TEXT[i][j])
        if isinstance(TEXT[i], list):
            TEXT[i] = '!'.join(TEXT[i])
    TEXT = '.'.join(TEXT)

    TEXT = TEXT.split(' \n ')
    text_copy = deepcopy(TEXT)
    maximum = find_maximum()
    if side == 'r':
        align_right(maximum, '')
    elif side == 'l':
        align_left(maximum, '')
    elif side == 'w':
        align_width(maximum, '')
    Menu(side, maximum)

def COUNT(text_mass, delim, counter=0):
    for i in range(len(text_mass)):
        counter = 0
        text_mass[i] = text_mass[i].split(delim)
        for j in range(len(text_mass[i])):
            if delim == '+' and counter == 0:
                COUNT(text_mass[i], '-')
                counter += 1
            text_mass[i][j] = text_mass[i][j].split(' ')
        j = 1
        while j < len(text_mass[i]):
            try:
                req_before, req_after = -1, 0
                while text_mass[i][j - 1][req_before] == '': req_before -= 1
                while text_mass[i][j][req_after] == '': req_after += 1
                first = int(text_mass[i][j - 1][req_before])
                second = int(text_mass[i][j][req_after])
                if '\n' in text_mass[i][j][req_after]:
                    text_mass[i][j].insert(req_after + 1, '\n')
                text_mass[i][j - 1][req_before] = str(
                    (first + second) * (delim == '+')
                    + (first - second) * (delim == '-'))
                while req_before != -1:
                    text_mass[i][j - 1].pop(-1)
                    req_before += 1
                while req_after != 0:
                    text_mass[i][j].pop(0)
                    req_after -= 1
                text_mass[i][j].pop(req_after)
                text_mass[i][j - 1].extend(text_mass[i][j])
                text_mass[i].pop(j)
            except ValueError:
                text_mass[i][j - 1] = ' '.join(text_mass[i][j - 1])
                j += 1
        text_mass[i][-1] = ' '.join(text_mass[i][-1])
        text_mass[i] = (delim).join(text_mass[i])

def count_sums_and_difference(max_len, side):
    global TEXT, text_copy
    RETURNING()
    for ending in ['.', '!', '?', ';', ',']:
        TEXT = ('\n'.join(TEXT)).split(ending)
        COUNT(TEXT, '+')
        TEXT = (ending.join(TEXT)).split('\n')

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
    try:
        menu = {1: align_left,
                2: align_right,
                3: align_width,
                4: replace_word,
                5: delete_word,
                6: count_sums_and_difference,
                7: delete_max_length_word_in_max_len_sentence}
        for i in range(len(menu)):
            print(i + 1, '-',
                  ' '.join(str(menu[i + 1]).split(' ')[1].split('_')))
        answer = int(input("Enter an appropriate dial to pick up an action:"))
        while answer not in menu:
            answer = int(input("Incorrect input. Try again:"))
        menu[answer](max_string_len, side)
    except ValueError:
        print("Incorrect input!")
Menu()
