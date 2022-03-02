import tkinter as tk
from tkinter import messagebox
import glob as gl
from random import random

root = tk.Tk()
root.geometry('300x200')
root.title("表白")

frame = tk.Frame(root)
frame.pack()
tk.Label(frame, text="To my love", font=25, padx=30, pady=30).pack(side=tk.LEFT, anchor=tk.N)
img = tk.PhotoImage(file="")
label = tk.Label(frame, image=img, padx=30, pady=30, bd=0)

ok = tk.Button(frame, text="Agree", fg='green')
ok.place(relx=0.2, rely=0.9, anchor=tk.CENTER)
no = tk.Button(frame, text="Desagree", fg='red')
no.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

# the second box
frame1 = tk.Frame(root)
frame1.pack()
tk.Label(frame1, text="I been wait for you  a longtime despite that \n I still miss you and \n want to get reunited",
         justify=tk.LEFT, fg='red', pady=50, padx=50).pack(side=tk.LEFT, anchor=tk.N)
exit = tk.Button(frame1, text="I want too", fg="green", command=root.quit).place(relx=0.3, rely=0.8)


def on_exit():
    messagebox.showwarning(title="Warning", message="You can't close the window")


root.protocol('WM_DELETE_WINDOW', on_exit)


def move(e):
    no.place(relx=random(), rely=random(), anchor=tk.CENTER)


no.bind('<Enter>', move)


# def exits(e):
#     exit.place(relx=random(), rely=random(), anchor=tk.CENTER)
# exit.bind('<Enter>', exits)


def route():
    frame.pack_forget()
    frame1.pack()


ok.config(command=route)

root.mainloop()
