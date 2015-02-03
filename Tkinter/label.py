#!/usr/bin/env python3
from tkinter import*

class MyGUI:
  def __init__(self):
    self.__mainWindow = Tk()
    #self.fram1 = Frame(self.__mainWindow)
    self.labelText = 'Enter amount to deposit'
    self.depositLabel = Label(self.__mainWindow, text = self.labelText)
    self.depositEntry = Entry(self.__mainWindow, width = 10)
    self.depositEntry.bind('<Return>', self.depositCallBack)
    self.depositLabel.pack()
    self.depositEntry.pack()


    mainloop()

  def depositCallBack(self,event):
    #self.labelText = 'change the value'
    self.depositLabel['text'] = 'change the value'
    print(self.labelText)




myGUI = MyGUI()

import tkinter as tk
from tkinter import *

def start(event):
    right = Label(screen, text = "Right")
    left = Label(screen, text = "Left")
    if event.keysym == "Right":
        left.destroy()
        right.pack()
    if event.keysym == "Left":
        right.destroy()
        left.pack()

screen = tk.Tk()
screen.bind_all("<Key>", start)
screen.mainloop()
