from tkinter import *
import time

root = Tk()
root.title('Clock')


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)


my_label = Label(root, text='Old Text')

my_label.pack(pady=20)

# my_label.after(2000, update)
clock()

root.mainloop()
