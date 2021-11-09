from tkinter import *

root = Tk()
root.title('Clock')


def update():
    my_label.config(text="New Text")


my_label = Label(root, text='Old Text')

my_label.pack(pady=20)

my_label.after(2000, update)

root.mainloop()
