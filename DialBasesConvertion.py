#!/usr/bin/env python3
from tkinter import *


def from7to10(dial):
    try:
        mult = 1
        dial = str(float(dial)).split('.')
        dial10 = 0
        dial[0] = dial[0].split('-')
        if len(dial[0]) == 2:
            mult = -1
            dial[0] = dial[0][-1]
        else:
            dial[0] = '-'.join(dial[0])
        for i in range(len(dial[0])):
            dial10 += int(dial[0][-(i + 1)]) * (7 ** i)
            if int(dial[0][-(i + 1)]) >= 7:
                raise UnicodeError
        for i in range(len(dial[1])):
            dial10 += int(dial[1][i]) * (7 ** (-(i + 1)))
            if int(dial[1][-(i + 1)]) >= 7:
                raise UnicodeError
        dial10 = float("{:.6f}".format(dial10))
        if str(dial10).split('.')[1] == '0':
            dial10 = int(dial10)
        dial10 *= mult
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
        mult = 1
        if dial[0][0] == '-':
            mult = -1
        before_dot = abs(int(dial[0]))
        after_dot = int(dial[1])
        required_dial = ''
        if before_dot == 0:
            required_dial += '0'
        while before_dot != 0:
            required_dial = str(before_dot % 7) + required_dial
            before_dot //= 7
        if after_dot != 0:
            required_dial += '.'
            after_dot = float('0.' + str(after_dot))
        iterations = 0
        while after_dot != 0.0 and iterations < 6:
            after_dot *= 7
            after_dot %= 7
            required_dial += str(int(after_dot))
            iterations += 1
        if len(required_dial.split('.')) == 1:
            required_dial = int(required_dial)*mult
        else:
            if mult == -1:
                required_dial = '-' + required_dial
        return required_dial
    except ValueError:
        return "Incorrect input"
    else:
        return "UNKNOWN MISTAKE"


def result(from_base, dial, output_field, butto, butfrom):
    dial = dial.get()
    butto.config(bg="blue")
    butfrom.config(bg="white")
    output_field.config(state="normal")
    output_field.delete(0, END)
    if from_base == 10:
        output_field.insert(0, from10to7(dial))
    else:
        output_field.insert(0, from7to10(dial))
    output_field.config(state="disabled")


def calc(dial, input_field, output_field):
    delete(1, output_field)
    input_field.insert(input_field.index(INSERT), str(dial))


def delete(input_field, output_field):
    if type(input_field) != int:
        input_field.delete(0, END)
    if type(output_field) != int:
        output_field.config(state="normal")
        output_field.delete(0, END)
        output_field.config(state="disabled")


def information(text = "автор"):
    info = Tk()
    plot_author = "Программу разработал Шевцов Егор, студент первого курса МГТУ" +\
                  " им. Баумана факультета ИУ7\n"
    plot_prog = "Данная программа реализует перевод действительных чисел из"+\
                " семеричной системы счисления в десятитчную и обратно\n" + \
                "Программа позволяет вводить данные как через обычную клавиатуру,"+\
                "так и через электронную."

    textwid = Text(info, wrap=WORD)
    if text == "автор":
        textwid.insert(END, plot_author)
    else:
        textwid.insert(END, plot_prog)
    textwid.config(state="disabled")
    textwid.grid(row=0, column=0)
    info.resizable(False, False)
    info.mainloop()


def window():
    root = Tk()
    root.title('Перевод чисел')
    BWIDTH, BHEIGHT = 12, 6

    #СОЗДАЮТСЯ ПОЛЯ ВВОДА И ВЫВОДА
    ifield = Entry(width=BWIDTH * 3)
    ifield.grid(row=0, column=0, columnspan=3)
    ofield = Entry(width=BWIDTH * 3)
    ofield.config(state="disabled")
    ofield.grid(row=1, column=0, columnspan=3)

    ifield.bind('<Key>', lambda aux=1, out=ofield: delete(1, out))

    #СОЗДАЮ И НАСТРАИВАЮ КНОПКИ-ЦИФРЫ ДЛЯ КАЛЬКУЛЯТОРА
    for i in range(1, 10):
        Button(root, text="{}".format(i), bg = "white", width=BWIDTH, height=BHEIGHT,
               command=lambda f=i, inp=ifield, out=ofield: calc(f, inp, out)).grid(
               row=(i - 1) // 3 + 3, column=(i - 1) % 3)
    Button(text="0", bg="white", width=BWIDTH, height=BHEIGHT,
           command=lambda f=0, inp=ifield, out=ofield:
           calc(f, inp, out)).grid(row=6, column=1)

    #КНОПКИ ПЕРЕВОДА ИЗ ОДНО СИСТЕМЫ СЧИСЛЕНИЯ В ДРУГУЮ
    seventoten = Button(text="7->10", bg="white", width=BWIDTH, height=BHEIGHT)
    seventoten.grid(row=2, column=0)
    tentoseven = Button(text="10->7", bg="white", width=BWIDTH, height=BHEIGHT)
    tentoseven.grid(row=2, column=2)
    tentoseven.config(command=lambda dial=ifield, out=ofield, base=10,
                      butto=tentoseven, butfrom=seventoten:
                      result(base, dial, out, butto, butfrom))
    seventoten.config(command=lambda dial=ifield, out=ofield, base=7,
                      butto=seventoten, butfrom=tentoseven:
                      result(base, dial, out, butto, butfrom))

    #КНОПКИ ОЧИСТКИ ВСЕХ ПОЛЕЙ, ДОБАВЛЕНИЯ ТОЧКИ И ЗНАКА МИНУС
    Button(text="clear", bg="white", width=BWIDTH, height=BHEIGHT,
           command=lambda inp=ifield,out=ofield:
           delete(inp, out)).grid(row=2, column=1)
    Button(text=".", bg="white", width=BWIDTH, height=BHEIGHT,
           command=lambda f='.', out=ofield, inp=ifield: calc(f, inp, out)).grid(
           row=6, column=0)
    Button(text="-", bg="white", width=BWIDTH, height=BHEIGHT,
           command=lambda f='-', out=ofield, inp=ifield: calc(f, inp, out)).grid(
           row=6, column=2)


    #СОЗДАЮ СТРОКУ ПАДАЮЩЕГО МЕНЮ И РАЗМЕЩАЮ ЕГО В ОСНОВНОМ ОКНЕ
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    #СОЗДАЮ МЕНЮ ДЕЙСТВИЯ С ПОДПУНКТАМИ ПЕРЕВОДА МЕЖДУ СИСТЕМАМИ СЧИСЛЕНИЯ
    action = Menu(mainmenu, tearoff=0)
    action.add_command(label="7->10", command=lambda dial=ifield, out=ofield,
                       base=7, butto=seventoten, butfrom=tentoseven:
                       result(base, dial, out, butto, butfrom))
    action.add_command(label="10->7", command=lambda dial=ifield, out=ofield,
                       base=10, butto=tentoseven, butfrom=seventoten:
                       result(base, dial, out, butto, butfrom))

    #СОЗДАЮ ПОДМЕНЮ С ОЧИСТКОЙ ПОЛЕЙ ВВОДА-ВЫВОДА И ДОБАВЛЯЮ В НЕГО ВОЗМОЖНОСТИ
    #ОЧИСТКИ КАЖДОГО ПОЛЯ КАК ПО ОТДЕЛЬНОСТИ, ТАК И ВМЕСТЕ
    clearmenu = Menu(action, tearoff=0)
    clearmenu.add_command(label="Очистить поле ввода", command=lambda inp=ifield,
                          out=ofield: delete(inp, 1))
    clearmenu.add_command(label="Очистить поле вывода",command=lambda inp=ifield,
                        out=ofield: delete(1, out))
    clearmenu.add_command(label="Очистить все поля", command=lambda inp=ifield,
                          out=ofield: delete(inp, out))
    action.add_cascade(label="Очистка полей ввода-вывода", menu=clearmenu)
    mainmenu.add_cascade(label="Действия", menu=action)

    #СОЗДАЮ ЕЩЕ ОДНО МЕНЮ, В КОТОРОМ МОЖНО УЗНАТЬ ИНФОРМАЦИЮ О ПРОГРАММЕ И ОБ АВТОРЕ
    info = Menu(mainmenu, tearoff=0)
    info.add_command(label="Информация о программе",
                     command=lambda param=0: information(param))
    info.add_command(label="Информация об авторе",
                     command=information)
    mainmenu.add_cascade(label="Информация", menu=info)

    root.resizable(False, False)
    root.mainloop()

window()
