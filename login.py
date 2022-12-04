import ctypes
from tkinter import *
from tkinter import messagebox
import ast
import utils

#ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title("Login")
window.geometry("1200x650+350+200")
window.configure(bg="#fff")
window.resizable(False,False)
#-----------------------------------
def login():
   username=user.get()
   password=pwd.get()

   result=utils.login(username,password)

   if result:
      messagebox.showinfo('Sign In','Successfully Logged In')
      window.destroy()
      if username=='admin':
         import main1
   else:
      messagebox.showerror('Sig In','Invalid credentials')

def show_signup():
   window.destroy()
   import signup

frame=Frame(window,width=500,height=500,bg='white')
frame.place(x=580,y=100)

img=PhotoImage(file='login.png')
Label(window,image=img,border=0,bg='white').place(x=120,y=140)

heading=Label(frame,text='Sign In', fg='#57a1f8',bg='white',font=('Cascadia Mono SemiBold',26,'bold'))
heading.place(x=100,y=0)

#---------------------------------
def on_enter(e):
   user.delete(0,'end')
def on_leave(e):
   if user.get()=='':
      user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Cascadia Mono Light',11))
user.place(x=30,y=120)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=430,height=2,bg='black').place(x=25,y=155)

#---------------------------------

def on_enter(e):
   pwd.delete(0,'end')
def on_leave(e):
   if pwd.get()=='':
      pwd.insert(0,'Password')

pwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Cascadia Mono Light',11))
pwd.place(x=30,y=185)
pwd.insert(0,'Password')
pwd.bind('<FocusIn>',on_enter)
pwd.bind('<FocusOut>',on_leave)

Frame(frame,width=430,height=2,bg='black').place(x=25,y=220)
#---------------------------------

Button(frame,width=33,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=login,font=('Cascadia Mono SemiBold',11)).place(x=22,y=275)
label=Label(frame,text='Dont have an account?',fg='black',bg='white',font=('Cascadia Mono Light',10))
label.place(x=60,y=345)

signup=Button(frame,width=7,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=('Cascadia Mono Light',9),command=show_signup)
signup.place(x=325,y=343)

window.mainloop()
