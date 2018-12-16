# -*- coding: <utf-8> -*-
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
            cur_file = codecs.open(PATH, encoding='utf8' 'w')
            print("File with name", '"', file_name, '"', "successfully created.")
            cur_file_name = file_name
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

    menu()


def print_all_information():
    global cur_file
    for text in cur_file:
        if text[-1] == '\n':
            text = text[:-2]
        else:
            text = text[:-1]
        text = [x for x in text.split('&')]
        for word in text:
            print(word, end=' ')
        print()
    menu()


def one_field_search():
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
    answer = int(input("Pick up an appropriate number:"))
    while answer not in menu:
        print("Incorrect input. An element with this number doesn't exist.")
        for i in range(1, len(menu) + 1):
            print(i, '-', ' '.join(((str(menu[i]).split())[1]).split('_')))
        answer = int(input("Try again:"))
    print()
    menu[answer]()

menu()
