import ctypes
from tkinter import *
from tkinter import messagebox
import ast
import utils

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()
window.title("SignUp")
window.geometry("1200x650+350+200")
window.configure(bg="#fff")
window.resizable(False,False)
#----------------------------------

def signup():
   username=user.get()
   password=pwd.get()
   cpassword=cpwd.get()

   if username.strip()=="" or password.strip()=="":
      messagebox.showerror('Sign Up','Fields cannot be empty')
   elif cpassword!=password:
      messagebox.showerror('Sign Up','You have entered different passwords')
   else:
      utils.add_user(username,password)
      messagebox.showinfo('Sign Up','Successfully signed up') 
   

def show_signin():
   window.destroy()
   import login


img=PhotoImage(file='signup.png')
Label(window,image=img,border=0,bg='white').place(x=120,y=140)

frame=Frame(window,width=500,height=490,bg='white')
frame.place(x=580,y=80)

heading=Label(frame,text='Sign Up', fg='#57a1f8',bg='white',font=('Cascadia Mono SemiBold',26,'bold'))
heading.place(x=100,y=0)

#---------------------------------
def on_enter(e):
   user.delete(0,'end')
def on_leave(e):
   if user.get()=='':
      user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Cascadia Mono Light',11))
user.place(x=30,y=100)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=430,height=2,bg='black').place(x=25,y=135)

#---------------------------------

def on_enter(e):
   pwd.delete(0,'end')
def on_leave(e):
   if pwd.get()=='':
      pwd.insert(0,'Password')

pwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Cascadia Mono Light',11))
pwd.place(x=30,y=160)
pwd.insert(0,'Password')
pwd.bind('<FocusIn>',on_enter)
pwd.bind('<FocusOut>',on_leave)

Frame(frame,width=430,height=2,bg='black').place(x=25,y=195)

#---------------------------------

def on_enter(e):
   cpwd.delete(0,'end')
def on_leave(e):
   if cpwd.get()=='':
      cpwd.insert(0,'Confirm Password')

cpwd = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Cascadia Mono Light',11))
cpwd.place(x=30,y=220)
cpwd.insert(0,'Confirm Password')
cpwd.bind('<FocusIn>',on_enter)
cpwd.bind('<FocusOut>',on_leave)

Frame(frame,width=430,height=2,bg='black').place(x=25,y=255)

#---------------------------------

Button(frame,width=33,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup,font=('Cascadia Mono SemiBold',11)).place(x=22,y=305)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Cascadia Mono Light',10))
label.place(x=80,y=370)

signin=Button(frame,width=8,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=('Cascadia Mono Light',9),command=show_signin)
signin.place(x=293,y=368)

window.mainloop()



