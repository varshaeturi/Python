#creating digital clock in python
#tkinter is a python module used to create GUI applications 
#tkinter provides a GUI interface -
#the way you create a GUL application using python is by using the tkinter module 
#tk is an open source toolkit -> widgets -> menus, buttons, windows, text field 
from tkinter import * 

# root = Tk() #TK constructor method, it will create a new top level widget 

# Label (root, text="Hello World!").pack()

# root.mainloop() #this will keep the window active 

from tkinter import ttk

from tkinter import font

import time 

import datetime 

def quit(*args):
    root.destroy()


def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d  %H:%M:%S"))
    # time =(time.strftime("%H: %M: %S"))

    txt.set(time)
    root.after(1000, clock_time)


root = Tk ()

root.attributes("-fullscreen", False)
root.configure(background='skyblue')
root.bind("x",quit)

root.after(1000, clock_time)


fnt = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground= 'pink', background='skyblue')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()


