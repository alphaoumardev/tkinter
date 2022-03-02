import tkinter as th
from tkinter import messagebox
import glob as gl
from random import random

root = th.Tk()

root.title("Calculator")
root.geometry("260x250")
root.attributes("-topmost", True)
root.attributes("-alpha", 0.9)

# root["background"] = "#ffffff"
result = th.StringVar()
# result.set("0")
th.Label(root, textvariable=result, justify=th.RIGHT, anchor=th.SE, font=20, height=2) \
    .grid(row=1, column=1, columnspan=4)

# first row
clear = th.Button(root, text="C", width=5, relief=th.FLAT, font=20, bg="gray")
back = th.Button(root, text="<--", width=5, relief=th.FLAT, font=20, bg="gray")
division = th.Button(root, text="/", width=5, relief=th.FLAT, font=20, bg="gray")
multiple = th.Button(root, text="*", width=5, relief=th.FLAT, font=20, bg="gray")
clear.grid(column=1, row=2, padx=4, pady=2)
back.grid(column=2, row=2, padx=4, pady=2)
division.grid(column=3, row=2, padx=4, pady=2)
multiple.grid(column=4, row=2, padx=4, pady=2)

# second row

seven = th.Button(root, text="7", width=5, relief=th.FLAT, font=20, bg="orange")
eight = th.Button(root, text="8", width=5, relief=th.FLAT, font=20, bg="orange")
nine = th.Button(root, text="9", width=5, relief=th.FLAT, font=20, bg="orange")
minus = th.Button(root, text="-", width=5, relief=th.FLAT, font=20, bg="gray")
seven.grid(column=1, row=3, padx=4, pady=2)
eight.grid(column=2, row=3, padx=4, pady=2)
nine.grid(column=3, row=3, padx=4, pady=2)
minus.grid(column=4, row=3, padx=4, pady=2)

# the third row
four = th.Button(root, text="4", width=5, relief=th.FLAT, font=20, bg="orange")
five = th.Button(root, text="5", width=5, relief=th.FLAT, font=20, bg="orange")
six = th.Button(root, text="6", width=5, relief=th.FLAT, font=20, bg="orange")
plus = th.Button(root, text="+", width=5, relief=th.FLAT, font=20, bg="gray")
four.grid(column=1, row=4, padx=4, pady=2)
five.grid(column=2, row=4, padx=4, pady=2)
six.grid(column=3, row=4, padx=4, pady=2)
plus.grid(column=4, row=4, padx=4, pady=2)

# the fourth row
one = th.Button(root, text="1", width=5, relief=th.FLAT, font=20, bg="orange")
two = th.Button(root, text="2", width=5, relief=th.FLAT, font=20, bg="orange")
three = th.Button(root, text="3", width=5, relief=th.FLAT, font=20, bg="orange")
equal = th.Button(root, text="=", width=5, height=3, relief=th.FLAT, font=20, bg="red")
one.grid(column=1, row=5, padx=4, pady=2)
two.grid(column=2, row=5, padx=4, pady=2)
three.grid(column=3, row=5, padx=4, pady=2)
equal.grid(column=4, row=5, padx=4, pady=2, rowspan=2)

# The last row

zero = th.Button(root, text="0", width=12, relief=th.FLAT, font=20, bg="orange")
dot = th.Button(root, text=".", width=5, relief=th.FLAT, font=20, bg="orange")
zero.grid(column=1, row=6, padx=4, pady=2, columnspan=2)
dot.grid(column=3, row=6, padx=4, pady=2)

# The logic of the calculator


zero.config(command=lambda: click_button('0'))
one.config(command=lambda: click_button('1'))
two.config(command=lambda: click_button('2'))
three.config(command=lambda: click_button('3'))
four.config(command=lambda: click_button('4'))
five.config(command=lambda: click_button('5'))
six.config(command=lambda: click_button('6'))
seven.config(command=lambda: click_button('7'))
eight.config(command=lambda: click_button('8'))
nine.config(command=lambda: click_button('9'))

minus.config(command=lambda: click_button('-'))
multiple.config(command=lambda: click_button('*'))
plus.config(command=lambda: click_button('+'))
division.config(command=lambda: click_button('/'))


def click_button(num):
    print(f"{num}")
    result.set(result.get() + num)


def cal():
    st = result.get()
    re = eval(st)
    result.set(str(re))


equal.config(command=cal)

root.mainloop()
