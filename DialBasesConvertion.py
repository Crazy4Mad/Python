#!/usr/bin/env python3
from tkinter import *

def from7to10(dial):
    try:
        dial = str(float(dial)).split('.')
        dial10 = 0
        for i in range(len(dial[0])):
            dial10 += int(dial[0][-(i + 1)]) * (7 ** i)
            if int(dial[0][-(i + 1)]) >= 7:
                raise UnicodeError

        for i in range(len(dial[1])):
            dial10 += int(dial[1][i]) * (7 ** (-(i + 1)))
            if int(dial[1][-(i + 1)]) >= 7:
                raise UnicodeError
        if str(dial10).split('.')[1] == '0':
            dial10 = int(dial10)
        return dial10

    except UnicodeError:
        return "This dial isn't in 7th base"
    except ValueError:
        return "Incorrect input"
    else:
        return "UNKNOWN MISTAKE"


def from10to7(dial):
    try:
        dial = str(float(dial)).split('.')
        aux = int(dial[0])
        dial7 = ''
        while aux != 0:
            dial7 = str(aux % 7) + dial7
            aux = int(aux / 7)
        aux = float('0.' + dial[1])
        dial7 += '.'
        iterations = 0
        while aux != 0.0 and iterations < 8:
            aux *= 7
            aux %= 7
            dial7 += str(int(aux))
            iterations += 1
        if dial7.split('.')[1] == '':
            dial7 = int(dial7.split('.')[0])
        return dial7
    except ValueError:
        return "Incorrect input"
    else:
        return "UNKNOWN MISTAKE"

root = Tk()

def result(from_base, dial, output_field):
    dial = dial.get()
    output_field.delete(0, END)
    if from_base == 10:
        output_field.insert(0, from10to7(dial))
    else:
        output_field.insert(0, from7to10(dial))


def calc(dial, input_field):
    input_field.insert(input_field.index(INSERT), str(dial))


def delete(input_field, output_field):
    input_field.delete(0, END)
    output_field.delete(0, END)


def window():
    root.title('Перевод чисел')

    bwidth, bheight = 12, 6

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="")

    input_field = Entry(width = bwidth*3)
    input_field.grid(row=0, column=0, columnspan=3)
    output_field = Entry(width = bwidth*3)
    output_field.grid(row=1, column=0, columnspan=3)

    for i in range(1, 10):
        but = Button(root, text="{}".format(i), width=bwidth, height=bheight,
                     command=lambda f=i, inp=input_field: calc(f, inp))
        but.grid(row=(i - 1) // 3 + 3, column=(i - 1) % 3)

    seven_ten = Button(text="7->10", width=bwidth, height=bheight,
                       command=lambda dial=input_field, out=output_field,
                                      base=7:
                       result(base, dial, out)).grid(row=2, column=0)
    zero = Button(text="0", width=bwidth, height=bheight,
                  command=lambda f=0, inp=input_field:
                  calc(f, inp)).grid(row=6, column=1)
    ten_seven = Button(text="10->7", width=bwidth, height=bheight,
                       command=lambda dial=input_field, out=output_field,
                                      base=10:
                       result(base, dial, out)).grid(row=2, column=2)

    clear = Button(text="clear", width=bwidth, height=bheight,
                   command=lambda inp=input_field, out=output_field: delete(inp,
                                                                            out))
    clear.grid(row=2, column=1)
    dot = Button(text=".", width=bwidth, height=bheight,
                 command=lambda f='.', inp=input_field: calc(f, inp)).grid(
        row=6, column=0)
    minus = Button(text="-", width=bwidth, height=bheight,
                   command=lambda f='-', inp=input_field: calc(f, inp)).grid(
        row=6, column=2)

    root.resizable(False, False)
    root.mainloop()

window()
