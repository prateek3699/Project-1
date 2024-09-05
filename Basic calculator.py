from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
            

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("385x344")
root.minsize(370,451)     #width * height
root.maxsize(370,451)     #width * height

root.title("Calculator By Prateek")
#root.wm_iconbitmap("1.ico")          #for icon change


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

frame1 = Frame(root, bg="grey")
button1 = Button(frame1, text="9", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button1.pack(side=LEFT, padx=2, pady=0)
button1.bind("<Button-1>", click)

button2 = Button(frame1, text="8", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button2.pack(side=LEFT, padx=15, pady=10)
button2.bind("<Button-1>", click)


button3 = Button(frame1, text="7", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button3.pack(side=LEFT, padx=10, pady=10)
button3.bind("<Button-1>", click)


button4 = Button(frame1, text="+", bg="red",padx=5, pady=5, font="lucida 20 bold")
button4.pack(side=LEFT, padx=15, pady=15)
button4.bind("<Button-1>", click)


button5 = Button(frame1, text="*", bg="red",padx=5, pady=5, font="lucida 20 bold")
button5.pack(side=LEFT, padx=15, pady=15)
button5.bind("<Button-1>", click)

frame1.pack()

frame2 = Frame(root, bg="grey")
button6 = Button(frame2, text="6", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button6.pack(side=LEFT, padx=2, pady=0)
button6.bind("<Button-1>", click)

button7 = Button(frame2, text="5", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button7.pack(side=LEFT, padx=15, pady=15)
button7.bind("<Button-1>", click)


button8 = Button(frame2, text="4", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button8.pack(side=LEFT, padx=15, pady=15)
button8.bind("<Button-1>", click)

button9 = Button(frame2, text="-", bg="red",padx=5, pady=5, font="lucida 20 bold")
button9.pack(side=LEFT, padx=10, pady=12)
button9.bind("<Button-1>", click)


button10 = Button(frame2, text="/", bg="red",padx=5, pady=5, font="lucida 20 bold")
button10.pack(side=LEFT, padx=20, pady=15)
button10.bind("<Button-1>", click)

frame2.pack()

frame3 = Frame(root, bg="grey")
button11 = Button(frame3, text="3", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button11.pack(side=LEFT, padx=2, pady=0)
button11.bind("<Button-1>", click)

button12 = Button(frame3, text="2", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button12.pack(side=LEFT, padx=15, pady=15)
button12.bind("<Button-1>", click)


button13 = Button(frame3, text="1", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button13.pack(side=LEFT, padx=15, pady=15)
button13.bind("<Button-1>", click)


button14 = Button(frame3, text="=", bg="red",padx=5, pady=5, font="lucida 20 bold")
button14.pack(side=LEFT, padx=16, pady=15)
button14.bind("<Button-1>", click)


button15 = Button(frame3, text="C", bg="red",padx=5, pady=5, font="lucida 20 bold")
button15.pack(side=LEFT, padx=5, pady=14)
button15.bind("<Button-1>", click)

frame3.pack()

frame4 = Frame(root, bg="grey")
button16 = Button(frame4, text="0",bg="yellow", padx=5, pady=5, font="lucida 20 bold")
button16.pack(side=LEFT, padx=3, pady=0)
button16.bind("<Button-1>", click)

button17 = Button(frame4, text=".", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button17.pack(side=LEFT, padx=15, pady=15)
button17.bind("<Button-1>", click)


button18 = Button(frame4, text="00", bg="yellow",padx=5, pady=5, font="lucida 20 bold")
button18.pack(side=LEFT, padx=15, pady=15)
button18.bind("<Button-1>", click)

button19 = Button(frame4, text="Error", padx=5, pady=5, font="lucida 20 bold")
button19.pack(side=LEFT, padx=17, pady=18)
button19.bind("<Button-1>", click)

frame4.pack()


root.mainloop()
