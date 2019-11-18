from Tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")

bclick = 0
flag = 0

def clear():
    global bclick, flag
    bclick = 0
    flag = 0
    a = '                    '
    txt = Label(tk,text=a,font=('Arial Bold',16))
    txt.grid(column=1,row=7)
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'


def disable():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick == 0:
        buttons["text"] = "X"
        bclick = 1
        Win()
        flag += 1


    elif buttons["text"] == " " and bclick == 1:
        buttons["text"] = "O"
        bclick = 0
        Win()
        flag += 1
    

def Win():
    if ((button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X') or
        (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X') or
        (button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X') or
        (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X') or
        (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X') or
        (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X') or
        (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X') or
        (button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X')):
	disable()        
	a = 'X Wins'
    	txt = Label(tk,text=a,font=('Arial Bold',16))
    	txt.grid(column=1,row=7)

    elif (flag == 8):
        a = 'Game is Tie'
    	txt = Label(tk,text=a,font=('Arial Bold',16))
    	txt.grid(column=1,row=7)

    elif ((button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O') or 
            (button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O') or
            (button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O') or 
            (button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O') or 
            (button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O') or 
            (button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O') or 
            (button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O') or 
            (button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O')):
	disable()
        a = 'O Wins'
    	txt = Label(tk,text=a,font=('Arial Bold',16))
    	txt.grid(column=1,row=7)

buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

button10 = Button(tk, text='Reset', font='Times 20 bold', bg='Green', fg='white',command=lambda: clear())
button10.grid(row=6, column=1)

tk.mainloop()
