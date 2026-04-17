from tkinter import *


root = Tk()
root.geometry("300x420")
root.configure(bg="black")

def click(num):
    e2.insert(30,num)
def click1(pro):
    e2.insert(30,pro)
def delete():
    e2.delete(0, END)
    
def result ():
    r = e2.get()
    res = eval(r)
    e2.delete(0, END)
    e2.insert(30, res)
        

e = Entry(root,border=0, font="Arial 19 bold", bg="black", fg="white", width=30)
e.pack()
e1 = Entry(root,border=0, font="Arial 19 bold", bg="black", fg="white", width=30,)
e1.pack()
e2 = Entry(root,border=0, font="Arial 25 bold", bg="black", fg="white", width=15, justify="right")
e2.place(x=20, y=60)

btn1 = Button(root,bg="#00D2D2", border= 0,text="CE",justify="center", fg="#0A1111", font="Arial 19 bold", width=4, height=1,command=lambda:delete() )
btn1.place(x=5, y=120)
btn2 = Button(root,bg="#00D2D2", border= 0,text="+",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("+") )
btn2.place(x=80, y=120)
btn3 = Button(root,bg="#00D2D2", border= 0,text="-", justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("-") )
btn3.place(x=155, y=120)
btn4 = Button(root,bg="#00D2D2", border= 0,text="/",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("/") )
btn4.place(x=230, y=120)

btn5 = Button(root,bg="#0A1111", border=0,text="7",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(7) )
btn5.place(x=5, y=180)
btn6 = Button(root,bg="#0A1111", border= 0,text="8",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(8) )
btn6.place(x=80, y=180)
btn7 = Button(root,bg="#0A1111", border= 0,text="9", justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(9) )
btn7.place(x=155, y=180)
btn8 = Button(root,bg="#00D2D2", border= 0,text="*",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("*") )
btn8.place(x=230, y=180)

btn9 = Button(root,bg="#0A1111", border=0,text="4",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(4) )
btn9.place(x=5, y=240)
btn10 = Button(root,bg="#0A1111", border= 0,text="5",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(5) )
btn10.place(x=80, y=240)
btn11 = Button(root,bg="#0A1111", border= 0,text="6", justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(6) )
btn11.place(x=155, y=240)
btn12 = Button(root,bg="#00D2D2", border= 0,text="%",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("%") )
btn12.place(x=230, y=240)

btn13 = Button(root,bg="#0A1111", border=0,text="1",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(1) )
btn13.place(x=5, y=300)
btn14 = Button(root,bg="#0A1111", border= 0,text="2",justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(2) )
btn14.place(x=80, y=300)
btn15 = Button(root,bg="#0A1111", border= 0,text="3", justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(3) )
btn15.place(x=155, y=300)
btn16 = Button(root,bg="#00D2D2", border= 0,text="^",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:click1("**") )
btn16.place(x=230, y=300)

btn17 = Button(root,bg="#0A1111", border= 0,text="0",justify="center", fg="white", font="Arial 19 bold", width=9, height=1,command=lambda:click(0) )
btn17.place(x=5, y=360)
btn18 = Button(root,bg="#0A1111", border= 0,text=".", justify="center", fg="white", font="Arial 19 bold", width=4, height=1,command=lambda:click(".") )
btn18.place(x=155, y=360)
btn19 = Button(root,bg="#00D2D2", border= 0,text="=",justify="center", fg="#2F3838", font="Arial 19 bold", width=4, height=1,command=lambda:result() )
btn19.place(x=230, y=360)









root.mainloop()

