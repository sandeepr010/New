from tkinter import *

tk = Tk()
tk.title("Factorial")
a = 1
b = 0
def fact():
    global a,b
    a = 1
    b = int(e1.get())
    for i in range(1,b+1):
        a = a*i
    txt = Label(tk,text=a,fg='red',font=20)
    txt.grid(row=3,column=0)

def clear():
    txt = Label(tk,text="                           ")
    txt.grid(row=3,column=0)

txt=Label(tk,text="Enter no : ",font=('Arial Bold',16))
txt.grid(row=1,column=0)

e1 = Entry(tk,width=10)
e1.grid(row=1,column=1)

btn = Button(tk,text='Enter',command=fact)
btn.grid(row=2,column=1)

btn = Button(tk,text='Clear',command=clear)
btn.grid(row=2,column=0)

tk.mainloop()
