from tkinter import *
import pymysql
import datetime
from tkinter import messagebox
import re
from email import message
regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
userID='urEmailDomain'
home='urHomeWindow'
fullEmail='urEmail'

def check(email):
    return bool(re.search(regex, email))
       
def login():
    global userID,fullEmail,user   
    try:
        connection= pymysql.connect(host='localhost',user='root',db='test2')
    except:
        print("start mysql server first...")
    else:
        print('connected successfully')
        print("Enter your Email and password")
        Email=user.get()
        Password=Pass.get()
        
        cur=connection.cursor()
        query="SELECT email,password FROM users"
        cur.execute(query)
        
        for (email,pas) in cur:
            
            if Email==email and Password==pas:
                
                login=True
                break
            else:
                login=False
        userID=(Email.split('@')[0])
        fullEmail=Email
        if login==True:
            print("Logged in successfully as",userID)
            newWindow()
        elif login==False:
            print("Email or password is wrong")
        cur.close()
        connection.close()
        
def submit_2():
    global fullEmail,book,writer
    try:
        connection= pymysql.connect(host='localhost',user='root',db='test2')
    except:
        print("start mysql server first...")
    else:
        cur=connection.cursor()
        query="insert into borrower4(book_name,writer_name,email,date) values(%s,%s,%s,%s)"
        str=format(datetime.datetime.now())
        val=[(book.get(),writer.get(),fullEmail,str)]
        cur.executemany(query,val)
        connection.commit()
        messagebox.showinfo("confermation", "Data inserted")


def submit_3():
    try:
        connection= pymysql.connect(host='localhost',user='root',db='test2')
    except:
        print("start mysql server first...")
    else:
        
        cur=connection.cursor()
        query="SELECT email,password FROM users"
        cur.execute(query)
        Email4=email2.get()
        for (email,pas) in cur:
            
            if Email4==email:
                
                login=False
                break
            else:
                login=True 
    if login==False:
        messagebox.showinfo("Error","Already regestered")
    elif not check(email2.get()):
        messagebox.showinfo("Error","Mail Incorrect")
    else:
        if len(email2.get())==0 or len(pass2.get())==0 or len(cpas.get())==0:
            messagebox.showinfo("required","All fields required")
        elif pass2.get()!=cpas.get():
            messagebox.showinfo("Password mismatch","Password mismatch")
        elif re.search(regex,email2.get())==True:
            messagebox.showinfo("Error","Invalid Email")
        else:
            connection= pymysql.connect(host='localhost',user='root',db='test2')
            cur=connection.cursor()
            query="insert into users(Email,Password) values(%s,%s)"
            val=[(email2.get(),pass2.get())]
            cur.executemany(query,val)
            connection.commit()
            messagebox.showinfo("confermation", "you registerd")
            connection.close()
            cur.close()


def registration():
    global email2,pass2,cpas,home3
    root.withdraw()
    home3=Toplevel(root)
    home3.title('borrow window')
    home3.geometry('500x600')
    Emailname=Label(home3,text="Email: ",font=('arial',10,'bold'),fg='blue').place(x=80,y=180)
    email2=Entry(home3,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    email2.place(x=210,y=180)
    password2=Label(home3,text="password: ",font=('arial',10,'bold'),fg='blue').place(x=80,y=230)
    pass2=Entry(home3,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    pass2.place(x=210,y=230)
    cpass=Label(home3,text="confurm password: ",font=('arial',10,'bold'),fg='blue').place(x=80,y=280)
    cpas=Entry(home3,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    cpas.place(x=210,y=280)
    submit3=Button(home3,text='submit',fg='white',bg='green',activebackground='blue',width=10,height=1,command=submit_3)
    submit3.place(x=200,y=380)
    logout2=Button(home3,text='Logout',fg='white',bg='red',activebackground='blue',width=10,height=1,command=logout_from_reg)
    logout2.place(x=400,y=20)

def borrow_book(): 
    global book,writer,home2
    home.withdraw()
    home2=Toplevel(root)
    home2.title('borrow window')
    home2.geometry('500x600')
    bookname=Label(home2,text="Book name: ",font=('arial',10,'bold'),fg='blue').place(x=120,y=180)
    book=Entry(home2,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    book.place(x=210,y=180)
    writername=Label(home2,text="writer name: ",font=('arial',10,'bold'),fg='blue').place(x=120,y=230)
    writer=Entry(home2,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    writer.place(x=210,y=230)
    submit2=Button(home2,text='submit',fg='white',bg='green',activebackground='blue',width=10,height=1,command=submit_2)
    submit2.place(x=200,y=280)
    logout=Button(home2,text='Logout',fg='white',bg='red',activebackground='blue',width=10,height=1,command=logout_from_borrow,compound=LEFT)
    logout.place(x=400,y=20)
    
  
def checkforid():
    global Pass2
    try:
        connection= pymysql.connect(host='localhost',user='root',db='test2')
    except:
        print("start mysql server first...")
    else:
            
        cur=connection.cursor()
        query="select * from users where Email=%s"
        val=[(Pass2.get())]
        cur.execute(query,val)
        record=cur.fetchall()
        if len(record)==1:
            messagebox.showinfo("Confermation", "Valid Email")
        else:
            messagebox.showinfo("Confermation", "Invalid Email")
            
def delete_from_list():
    global Pass3,Pass4
    try:
        connection= pymysql.connect(host='localhost',user='root',db='test2')
    except:
        print("start mysql server first...")
    else:
            
        cur=connection.cursor()
        query="delete from borrower4 where email = %s and book_name=%s"
        val=[(Pass3.get(),Pass4.get())]
        cur.executemany(query,val)
        messagebox.showinfo("Confermation", "Deleted")
        connection.commit()
        connection.close()
        cur.close()  
            
            
def newWindow():
    global userID,home,Pass2,Pass3,Pass4
    root.withdraw()
    home=Toplevel(root)
    home.title('Main Window')
    home.geometry('500x600')
    home.config(bg='azure')
    something=Label(home,text="You are logged in \n{}".format(userID),fg='green',bg='azure')
    something.place(x=120,y=20)
    logout=Button(home,text='Logout',fg='white',bg='red',activebackground='blue',width=10,height=1,command=logOut,compound=LEFT)
    logout.place(x=400,y=20)
    borrow=Button(home,text='Borrow Book',fg='white',bg='green',activebackground='green',width=10,height=1,command=borrow_book)
    borrow.place(x=190,y=100)
    something2=Label(home,text="Check in borrow list: ",fg='blue',bg='azure')
    something2.place(x=150,y=170)
    label2=Label(home,text="Email: ",fg='blue',bg='azure')
    label2.place(x=100,y=200)
    Pass2=Entry(home,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    Pass2.place(x=180,y=200)
    check=Button(home,text='Check',fg='white',bg='green',activebackground='green',width=10,height=1,command=checkforid)
    check.place(x=190,y=250)
    something3=Label(home,text="Delete from borrow list:  ",fg='blue',bg='azure')
    something3.place(x=150,y=320)
    label3=Label(home,text="Email: ",fg='blue',bg='azure')
    label3.place(x=100,y=350)
    Pass3=Entry(home,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    Pass3.place(x=180,y=350)
    label4=Label(home,text="Book name: ",fg='blue',bg='azure')
    label4.place(x=100,y=400)
    Pass4=Entry(home,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
    Pass4.place(x=180,y=400)
    check2=Button(home,text='Delete',fg='white',bg='green',activebackground='green',width=10,height=1,command=delete_from_list)
    check2.place(x=190,y=450)
    


def logout_from_borrow():
    global home2
    home2.withdraw()
    root.deiconify()
    print("Logged out successfully..")

def logout_from_reg():
    global home3
    home3.withdraw()
    root.deiconify()
    print("Logged out successfully..")

def logOut():
    global home
    home.withdraw()
    root.deiconify()
    print("Logged out successfully..")
    
root=Tk()
root.config(bg='blue')
root.title('Login Window')
root.geometry('530x430')
root.resizable(0, 0)

bgLabel=Label(root)
bgLabel.place(x=0,y=0)
nametag=Label(root,text="tamim",font=('arial',10,'bold'),fg='blue').place(x=120,y=180)

site=Label(root,text='Log in',font=('arial',15,'bold','underline'),fg='blue3')
site.place(x=220,y=120)

username=Label(root,text="Username: ",font=('arial',10,'bold'),fg='blue').place(x=120,y=180)
user=Entry(root,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
user.place(x=200,y=180)


password=Label(root,text="Password: ",font=('arial',10,'bold'),fg='blue').place(x=120,y=230)
Pass=Entry(root,width=30,font=('calibri',12),highlightbackground='blue',highlightthickness=1)
Pass.place(x=200,y=230)


submit=Button(root,text='Login',fg='white',bg='green',activebackground='blue',width=10,height=1,command=login,compound=LEFT)
submit.place(x=200,y=280)

reg=Button(root,text='registration',fg='white',bg='green',activebackground='blue',width=10,height=1,command=registration,compound=LEFT)
reg.place(x=300,y=280)

root.mainloop()