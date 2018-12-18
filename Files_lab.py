import os, codecs
cur_file = ''
cur_file_name = ''
FILES_SAVING_PATH = os.path.dirname(os.path.realpath("Files.py")) + '\\'


def choose_file():
    global cur_file, cur_file_name, FILES_SAVING_PATH
    file_name = input("Enter a name of file you want to open:")
    try:
        cur_file.close()
    except:
        pass
    try:
        PATH = FILES_SAVING_PATH + file_name + '.txt'
        cur_file = codecs.open(PATH, 'r', encoding='utf8')
        cur_file_name = file_name
    except:
        print("The file with this name doesn't exist.")
    menu()


def create_new_file():
    global cur_file, cur_file_name, FILES_SAVING_PATH
    file_name = input("Enter the file name you want to create:")
    try:
        PATH = FILES_SAVING_PATH + file_name + '.txt'
        open_file = codecs.open(PATH, 'r', encoding='utf8')
        print("The file with this name already exists or can't be created.")
        open_file.close()
    except FileNotFoundError:
        try:
            PATH = FILES_SAVING_PATH + file_name + '.txt'
            cur_file = codecs.open(PATH, 'w', encoding='utf8')
            print("File with name", '"', file_name, '"', "successfully created.")
            cur_file.close()
        except FileNotFoundError:
            print("Can't create the file with this name.")
        except OSError:
            print("Can't create the file with this name.")
        else:
            pass
    else:
        pass
    menu()


def add_information():
    global cur_file, cur_file_name, FILES_SAVING_PATH
    try:
        cur_file.close()
        cur_file = codecs.open(FILES_SAVING_PATH + cur_file_name + '.txt',
                               'a', encoding='utf8')
        string_to_write = ''
        cur_string = ''
        while cur_string != '.':
            cur_string = input("Enter the Second name (enter a dot to end information "
                "adding:")
            if cur_string != '.':
                string_to_write += cur_string + '&'
                cur_string = input("Enter the name:")
                string_to_write += cur_string + '&'
                try:
                    cur_string = input("Enter the math grade:")
                    int(cur_string)
                    string_to_write += cur_string + '&'
                    cur_string = input("Enter the programming grade:")
                    int(cur_string)
                    string_to_write += cur_string + '&'
                    cur_string = input("Enter the algebra grade:")
                    int(cur_string)
                    string_to_write += cur_string
                    cur_file.write(string_to_write + '\n')
                except:
                    print("Incorrect input. Informations' adding ended.")
                    break
                string_to_write = ''
        cur_file.close()
        cur_file = codecs.open(FILES_SAVING_PATH + cur_file_name + '.txt',
                               'r', encoding='utf8')
    except:
        pass
    menu()


def print_all_information():
    global cur_file
    for text in cur_file:
        if text[-1] == '\n':
            text = text[:-1]
        if text[-1] == '\r':
            text = text[:-1]
        text = [x for x in text.split('&')]
        for word in text:
            print(word, end=' ')
        print()
    cur_file.seek(0)
    menu()


def one_field_search():
    global cur_file_name, cur_file
    if cur_file_name != '':
        counter = 1
        for text in ["second name", "name", "math grade", "programming grade",
                     "algebra grade"]:
            print(counter, '-', text)
            counter += 1
        try:
            answer = int(
                input("Choose the field you are going to search for info:"))
        except:
            answer = 0
        while answer not in range(1, 6, 1):
            print("Incorrect input. The field on this number doesn't exist.")
            try:
                answer = int(input("Try again:"))
            except:
                answer = 0
        key = input('Enter the info you want to be found out:')
        if answer > 2:
            try:
                key = int(key)
                key = str(key)
            except:
                print("Incorrect input. There are only dials in this field.")
                return 0
        founded = False
        for text in cur_file:
            text = text.split('&')
            if text[-1][-1] == '\n':
                text[-1] = text[-1][:-1]
            if text[-1][-1] == '\r':
                text[-1] = text[-1][:-1]
            if str(text[answer - 1]) == key:
                founded = True
                print(' '.join(text))
        cur_file.seek(0)
        if not founded:
            print("No strings with this parameters")
    menu()


def two_field_search():
    menu()


def shut_down_the_program():
    try:
        cur_file.close()
    except:
        pass
    print("Goodbye")


def menu():
    if cur_file != '':
        print("\nCurrent file:\n", cur_file_name, sep='', end='\n\n')
    else:
        print('\nNo file was opened.\n')
    menu = {1: choose_file,
            2: create_new_file,
            3: add_information,
            4: print_all_information,
            5: one_field_search,
            6: two_field_search,
            7: shut_down_the_program}
    for i in range(1, len(menu) + 1):
        print(i, '-', ' '.join(((str(menu[i]).split())[1]).split('_')))
    try:
        answer = int(input("Pick up an appropriate number:"))
    except:
        answer = 0
    while answer not in menu:
        print("Incorrect input. An element with this number doesn't exist.")
        for i in range(1, len(menu) + 1):
            print(i, '-', ' '.join(((str(menu[i]).split())[1]).split('_')))
        answer = int(input("Try again:"))
    print()
    menu[answer]()

menu()
