from tkinter import *
from tkinter import ttk
import os

#myhost = os.uname()[1][:5] alito-v
def main(x):
    if (x == "ps"):
        go_ps()
    if (x == "ps_by_user"):
        go_ps_by_user()
    if (x == "ID_All_Proc"):
        go_ID_All_Proc()
    if (x == "Send_Signal_To_Proc"):
        go_Send_Signal_To_Proc()
    if (x == "stop_proc"):
        go_stop_proc()

def go_Send_Signal_To_Proc():
    c = open("signal.txt", "r")
    cont = c.read()
    window1 = Tk()
    window1.title("Signal")
    lable = Label(window1, text="Signal", fg="red")
    lable.grid(row=0, column=0)
    textbox = Text(window1, height=6, width=50)
    textbox.grid(row=1, column=1)
    textbox.insert(END,cont)
    lable1 = Label(window1, text="Choose the number of the signal:", fg="red")
    lable1.grid(row=2, column=0)
    listbox = Listbox(window1)
    listbox.grid(row=3, column=1)
    lable2 = Label(window1, text="Enter process name:", fg="red")
    lable2.grid(row=4, column=0)
    textbox = Text(window1, height=1, width=50)
    textbox.grid(row=5, column=1)
    btn = Button(window1, text="Ok", fg="red", command=lambda: help_go_stop_proc(textbox.get("1.0", "end-1c")))
    btn.grid(row=2, column=1)

def go_stop_proc():
    window1 = Tk()
    window1.title("Process")
    lable =Label(window1, text= "Enter process name" , fg = "red")
    lable.grid(row = 0,column = 0)
    textbox = Text(window1,height=1,width = 25)
    textbox.grid(row = 1,column = 1) 
    btn=Button(window1,text="Ok" ,fg="red" ,command=lambda :help_go_stop_proc (textbox.get("1.0","end-1c")) )
    btn.grid(row = 2,column = 1)
    window1.geometry("400x100")
def help_go_stop_proc(x):
    a=os.popen("ps -u"+x).read()
    show(a)
def go_ID_All_Proc():
    x = "pgrep -u"+myhost+" -l"
    a = os.popen(x).read()
    show(a)
def go_ps():
    a = os.popen("ps").read()
    show(a)

def go_ps_by_user():
    window1 = Tk()
    window1.title("User")
    lable =Label(window1, text= "Enter user name" , fg = "red")
    lable.grid(row = 0,column = 0)
    textbox = Text(window1,height=1,width = 25)
    textbox.grid(row = 1,column = 1) 
    btn=Button(window1,text="Ok" ,fg="red" ,command=lambda :help_go_ps_by_user (textbox.get("1.0","end-1c")) )
    btn.grid(row = 2,column = 1)
    window1.geometry("400x100")
def help_go_ps_by_user(x):
    a=os.popen("ps -u"+x).read()
    show(a)
def show(a):
    window = Tk()
    window.title("Result")
    text = Text(window,width = 50,height = 10)
    text.insert(END,a)
    text.pack()
    btn1=Button(window,text="ok" ,fg="red" ,command = lambda : close(window))
    btn1.pack()
def close(root):
    root.destroyed()
root = Tk()
root.title("test")
thelable = Label(root, text= "Choose your command :" , fg = "red")
thelable.grid(row = 0)
combobox = ttk.Combobox(root,values=["ps","ps_by_user","ID_All_Proc","stop_proc","Send_Signal_To_Proc"])
combobox.grid(row = 1,column = 1)
button1 = Button(root, text="Ok" , fg = "red" , command =lambda : main(combobox.get()) )
button1.grid(row = 2,column = 1)
root.geometry("400x100")

root.mainloop()

