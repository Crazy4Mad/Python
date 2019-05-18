from tkinter import *

def choice_sort(mass):
    cur_min, cur_min_ind = 0, 0
    for i in range(len(mass)):
        if int(mass[i]) == mass[i]:
            mass[i] = int(mass[i])
    for i in range(len(mass)):
        cur_min, cur_min_ind = mass[i], i
        for j in range(i + 1, len(mass)):
            if cur_min > mass[j]:
                cur_min, cur_min_ind = mass[j], j
        mass[i], mass[cur_min_ind] = mass[cur_min_ind], mass[i]
    return mass

def len_check(length_entry, status_entry, entries, count):
    try:
        status_entry["state"] = "normal"
        status_entry.delete(0, END)
        a = int(length_entry.get())
        if (a < 1 or a > 10):
            status_entry.insert(END, "Amount must be between 1 and 10")
            count["state"] = "disabled"
        else:
            for i in range(a):
                entries[i]["state"] = "normal"
            for i in range(a, 10):
                entries[i].delete(0, END)
                entries[i]["state"] = "disabled"
            entries[-1] = a
            count["state"] = "normal"

    except ValueError:
        status_entry.insert(END, "Amount must be integer")
        count["state"] = "disabled"
    status_entry["state"] = "disabled"


def check(entries, output):
    mass = []
    for i in range(entries[-1]):
        mass.append(entries[i].get())
    if entries[-1] > 10:
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
    for i in range(len(mass)):
        output[i]["state"] = "normal"
        output[i].delete(0, END)
        output[i].insert(END, mass[i])
        output[i]["state"] = "disabled"


def menu():
    root = Tk()
    ENTRY_WIDTH = 14
    entries_input, entries_output = [], []

    label = Label(text="Кол-во элементов", width = 14)
    label.grid(row = 0, column = 5)
    amount = Entry(width = ENTRY_WIDTH, justify="center")
    amount.grid(row = 1, column = 5)
    status = Entry(width=ENTRY_WIDTH*3, justify="center", state="disabled")
    status.grid(row=3, column=4, columnspan = 3)
    admit = Button(text="Принять", command=lambda:len_check(amount, status, entries_input, count))
    admit.grid(row = 2, column = 5)

    for i in range(10):
        entries_input.append(Entry(state="disabled", width = ENTRY_WIDTH,
                             justify="center"))
        entries_input[i].grid(row = 5, column = i)
        entries_output.append(Entry(state="disabled", width=ENTRY_WIDTH,
                            justify="center"))
        entries_output[i].grid(row = 7, column = i)
        label = Label(text = str(i + 1), width=14)
        label.grid(row = 4, column = i)
    entries_input.append(0)

    count = Button(text="Отсортировать", state="disabled",
                   command=lambda:check(entries_input, entries_output))
    count.grid(row = 6, column=5)
    root.resizable(False, False)
    root.mainloop()

menu()