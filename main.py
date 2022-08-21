import ctypes
from tkinter import *
from tkinter import messagebox
import ast
import utils


window = Tk()
window.title("Library Management")
window.geometry("1280x800")
window.resizable(True,True)
#-------------------------------------


fl = Frame(window,width='300',height='800',bg='black').place(x=0,y=0)
fr = Frame(window,width='980',height='800',bg='#eeeeee').place(x=300,y=0)
#---------------------------------

def on_enter(e):
   search_bar.delete(0,'end')
def on_leave(e):
   if search_bar.get()=='':
      search_bar.insert(0,'Search')

search_bar = Entry(fr,width=50,fg='black',border=0,bg='#eeeeee',
            font=('Cascadia Mono Light',16))
search_bar.place(x=350,y=20)
search_bar.insert(0,'Search')
search_bar.bind('<FocusIn>',on_enter)
search_bar.bind('<FocusOut>',on_leave)

Frame(fr,width=600,height=2,bg='black').place(x=350,y=50)

