from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title('Login Page')

root.geometry('925x500')
root.configure(bg='#fff')
root.resizable(False,False)



img=PhotoImage(file="C:\\Users\\welcome\\Downloads\\login.png")# u can give ur image path 
Label(root,image=img,bg='#fff').place(x=50,y=60)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="blue",bg='white',font=('Times New Roman',23))
heading.place(x=150,y=20)


def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"username")
user=Entry(frame,width=30,fg='black',border=0,bg='white',font=('Times New Roman',23,'bold'))
user.place(x=30,y=60)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
user.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    usep.delete(0,'end')

def on_leave(e):
    name=usep.get()
    if name=="":
        usep.insert(0,"password")

usep=Entry(frame,width=30,fg='black',border=0,bg='white',font=('Times New Roman',23,'bold'))
usep.place(x=30,y=130)
usep.bind('<FocusIn>',on_enter)
usep.bind('<FocusOut>',on_leave)
usep.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def signin():
    username=user.get()
    password=usep.get()

    if username=="admin" and password=="password":
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500')
        screen.config(bg='white')
        Label(screen,text="Application Under Construction",fg='Brown',font=('Chiller',40,'bold')).pack(expand=True)
        screen.mainloop()
    elif username!="" and password!="":
        messagebox.showerror('Login Failed','Invalid username or password')

Button(frame,width=39,pady=7,text='sign in',bg='blue',fg='white',border=0,command=signin,cursor='hand2').place(x=40,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Times New Roman',10))
label.place(x=50,y=249)



def signup():
    page1=Toplevel(root)
    page1.title("Sign up")
    page1.geometry("930x550")
    page1.configure(bg='#fff')
    page1frame=Frame(page1,width=550,height=930,bg='white')
    page1frame.place(x=200,y=150)
    page1.resizable(False,True)
    
    def on_ent(e):
       firstname.delete(0,'end')
    def on_leav(e):
       name=firstname.get()
       if name=="":
        firstname.insert(0,"First name")
    
    firstname=Entry(page1frame,width=100,fg='red',border=0,bg='white',font=('Times New Roman',18))
    firstname.place(x=30,y=30)
    firstname.bind('<FocusIn>',on_ent)
    firstname.bind('<FocusOut>',on_leav)
    firstname.insert(0,'First name')
    Frame(page1frame,width=230,height=1,bg='black').place(x=25,y=60)

    def on_ent(e):
       lastname.delete(0,'end')
    def on_leav(e):
        name=lastname.get()
        if name=="":
            lastname.insert(0,"Last name")

    lastname=Entry(page1frame,width=100,fg='red',border=0,bg='white',font=('Times New Roman',18))
    lastname.place(x=270,y=30)
    lastname.bind('<FocusIn>',on_ent)
    lastname.bind('<FocusOut>',on_leav)
    lastname.insert(0,'Last name')
    Frame(page1frame,width=250,height=1,bg='black').place(x=270,y=60)

    def on_ent(e):
       emailid.delete(0,'end')
    def on_leav(e):
       name=emailid.get()
       if name=="":
        emailid.insert(0,"Email Id name")
        
    emailid=Entry(page1frame,width=100,fg='red',border=0,bg='white',font=('Times New Roman',18))
    emailid.place(x=30,y=90)
    emailid.bind('<FocusIn>',on_ent)
    emailid.bind('<FocusOut>',on_leav)
    emailid.insert(0,'Emai Id')
    Frame(page1frame,width=500,height=1,bg='black').place(x=25,y=120)

    def on_ent(e):
       password.delete(0,'end')
    def on_leav(e):
       name=password.get()
       if name=="":
        password.insert(0,"Password")

    password=Entry(page1frame,width=100,fg='red',border=0,bg='white',font=('Times New Roman',18))
    password.place(x=30,y=150)
    password.bind('<FocusIn>',on_ent)
    password.bind('<FocusOut>',on_leav)
    password.insert(0,'Password')
    Frame(page1frame,width=500,height=1,bg='black').place(x=25,y=180)

    def on_ent(e):
       state.delete(0,'end')
    def on_leav(e):
       name=state.get()
       if name=="":
        state.insert(0,"Conform password")

    ConformPassword=Entry(page1frame,width=40,fg='red',border=0,bg='white',font=('Times New Roman',18))
    ConformPassword.place(x=30,y=210)
    ConformPassword.bind('<FocusIn>',on_ent)
    ConformPassword.bind('<FocusOut>',on_leav)
    ConformPassword.insert(0,'Conform Password')
    Frame(page1frame,width=500,height=1,bg='black').place(x=25,y=240)
    Button(page1frame,width=39,pady=7,text='Login',bg='red',fg='white',border=0,command=signin,cursor='hand2').place(x=50,y=300)
    page1.mainloop()
sign_up=Button(frame,width=0,text='Signup',border=0,bg='white',cursor='hand2',fg='blue',command=signup)
sign_up.place(x=180,y=249)




root.mainloop()
