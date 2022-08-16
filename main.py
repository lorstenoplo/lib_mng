import ctypes
from tkinter import *
from tkinter import messagebox
import ast
import utils

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title("Library mng")
window.geometry("1200x650+350+200")
window.configure(bg="#fff")
window.resizable(False,False)
#-------------------------------------

heading=Label(window,text='Welcome', fg='#57a1f8',bg='white',font=('Cascadia Mono SemiBold',26,'bold'))
heading.place(x=100,y=0)


window.mainloop()

