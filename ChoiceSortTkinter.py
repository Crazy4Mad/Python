from tkinter import *
import math

def Choice_sort(array):
    for i in range(len(array)):
        minim, min_ind = array[i], i
        for j in range(i + 1, len(array)):
            if array[j] < minim:
                minim = array[j]
                min_ind = j
        array[min_ind], array[i] = array[i], array[min_ind]
    return array

def Check(array_entry, amount_entry):
    try:
        aux = float(amount_entry)
        amount_entry = int(amount_entry)
        if abs(aux - amount_entry) != 0:
            raise ValueError
        if not(amount_entry >= 1 and amount_entry <= 10):
            raise ValueError

        array_entry = array_entry.split()
        if len(array_entry) != amount_entry:
            raise UnicodeError
        try:
            for i in range(amount_entry):
                float_aux = float(array_entry[i])
                int_aux = int(float_aux)
                if int_aux != aux:
                    array_entry[i] = int(array_entry[i])
                else:
                    array_entry[i] = float(array_entry[i])

            return Choice_sort(array_entry)
        except ValueError:
            root = Tk()
            Message(root, text="Некорректные данные: в массиве могут быть "\
                               "только числа").pack()
            root.resizable(False, False)
            root.mainloop()

    except UnicodeError:
        root = Tk()
        Message(root, text="Количество элементов в массиве и указанное количество не совпадают").pack()
        root.resizable(False, False)
        root.mainloop()

    except ValueError:
        root = Tk()
        Message(root, text="Некорректные данные: в окошке 'кол-во' должно быть введено "\
                      "целое число от 1 до 10").pack()
        root.resizable(False, False)
        root.mainloop()

def output_field_manip(output_field, array_entry=1, amount_entry = 1, flag=True):
    output_field["state"] = "normal"
    if flag:
        output_field.delete(0, END)
    else:
        output_field.insert(END, Check(array_entry.get(), amount_entry.get()))
    output_field["state"] = "disabled"

def Menu():
    root = Tk()
    BUTTON_WIDTH, BUTTON_HEIGHT = 6, 3

    Button(text="sort", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
           command=lambda: output_field_manip(output_entry, array_entry, amount_entry,
                                              False)).pack(side=BOTTOM)

    output_entry = Entry(state="disabled")
    output_entry.pack(side=BOTTOM)

    output_text = Label(text="Результат:")
    output_text.pack(side=BOTTOM)

    array_entry = Entry()
    array_entry.pack(side=BOTTOM)
    array_entry.bind('<Key>', lambda out=1: output_field_manip(output_entry))

    array_text = Label(text="Введите массив, разделяя элементы пробелами")
    array_text.pack(side=BOTTOM)

    amount_text = Label(text="Кол-во элементов в массиве")
    amount_text.pack(side=LEFT)

    amount_entry = Entry(width=BUTTON_WIDTH)
    amount_entry.pack(side=LEFT)
    amount_entry.bind('<Key>', lambda out=1: output_field_manip(output_entry))

    root.resizable(False, False)
    root.mainloop()

Menu()
