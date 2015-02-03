#!/usr/bin/env python3
from tkinter import *

master = Tk()

def callback(number):
    #import tkinter.messagebox
    print("clicked: " + str(number))
    #variable = messagebox.showinfo('foo')
    #return number

b = Button(master, text="0", command=lambda: callback(0)).pack()
c = Button(master, text="1", command=lambda: callback(1)).pack()
d = Button(master, text="2", command=lambda: callback(2)).pack()
e = Button(master, text="3", command=lambda: callback(3)).pack()
f = Button(master, text="4", command=lambda: callback(4)).pack()
g = Button(master, text="5", command=lambda: callback(5)).pack()
h = Button(master, text="6", command=lambda: callback(6)).pack()
i = Button(master, text="7", command=lambda: callback(7)).pack()
j = Button(master, text="8", command=lambda: callback(8)).pack()
k = Button(master, text="9", command=lambda: callback(9)).pack()

mainloop()
