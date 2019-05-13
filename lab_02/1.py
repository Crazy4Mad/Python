from tkinter import *

def choice_sort(mass):
    cur_min, cur_min_ind = 0, 0
    for i in range(len(mass)):
        if abs(int(mass[i]) - mass[i]) < 1e-5:
            mass[i] = int(mass[i])
        cur_min, cur_min_ind = mass[i], i
        for j in range(i + 1, len(mass)):
            if cur_min > mass[j]:
                cur_min, cur_min_ind = mass[j], j
        mass[i], mass[cur_min_ind] = mass[cur_min_ind], mass[i]
    return mass

def check(mass, output):
    mass = [x for x in mass.split()]
    if len(mass) > 10:
        output["state"] = "normal"
        output.delete(0, END)
        output.insert(END, "Больше 10 элементов")
        output["state"] = "disabled"
        return 0
    try:
        for i in range(len(mass)):
            mass[i] = float(mass[i])
        min_result(mass, output)
    except ValueError:
        output["state"] = "normal"
        output.delete(0, END)
        output.insert(END, "Неверный тип элемента")
        output["state"] = "disabled"

def min_result(mass, output):
    choice_sort(mass)
    mass = [str(x) for x in mass]
    mass = ' '.join(mass)
    output["state"] = "normal"
    output.delete(0, END)
    output.insert(END, mass)
    output["state"] = "disabled"


def menu():
    root = Tk()

    TEXT_ARR = ["Введите элементы через пробел", "Результат"]
    ENTRY_SIZES = [30, 30]
    ENTRIES_TYPES = ["normal", "disabled"]
    labels, fields = [], []
    for i in range(len(TEXT_ARR)):
        labels.append(Label(text=TEXT_ARR[i], justify="center"))
        labels[i].grid(row = i*2, column = 0)
        fields.append(Entry(width = ENTRY_SIZES[i], state=ENTRIES_TYPES[i]))
        fields[i].grid(row = i*2 + 1, column = 0)
    count = Button(text="Отсортировать", command = lambda:check(fields[0].get(), fields[1]))
    count.grid(row = len(TEXT_ARR)*2, column = 0)
    root.resizable(False, False)

    root.mainloop()

menu()