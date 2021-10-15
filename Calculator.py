import tkinter
screen = tkinter.Tk()
screen.title("Calculator")
screen.configure(bg= "orange")
screen.resizable(False,False)
expres = ""
def key(event):
    global expres
    expres += event.char
    lable["text"]=expres
def add(value):
    global expres
    expres += str(value)
    lable["text"]=expres
def reset():
    global expres
    expres = ""
    lable["text"]=expres
def calculate():
    global expres
    expres = eval(expres)
    lable["text"]=expres
    expres = str(expres)
def cal(event):
    calculate()
screen.bind("<Key>",key)
screen.bind("<Return>", cal)
lable = tkinter.Label(screen,text="",height= 4,width= 43,bg= "white",fg= "black",font= ("aerial",10,"normal"),borderwidth=2,relief="solid")
lable.grid(row=0,column= 0,columnspan= 4)
button1 = tkinter.Button(screen,text="1",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("1"))
button1.grid(row=1,column= 0)
button2 = tkinter.Button(screen,text="2",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("2"))
button2.grid(row=1,column= 1)
button3 = tkinter.Button(screen,text="3",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("3"))
button3.grid(row=1,column= 2)
button4 = tkinter.Button(screen,text="4",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("4"))
button4.grid(row=2,column= 0)
button5 = tkinter.Button(screen,text="5",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("5"))
button5.grid(row=2,column= 1)
button6 = tkinter.Button(screen,text="6",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("6"))
button6.grid(row=2,column= 2)
button7 = tkinter.Button(screen,text="7",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("7"))
button7.grid(row=3,column= 0)
button8= tkinter.Button(screen,text="8",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("8"))
button8.grid(row=3,column= 1)
button9 = tkinter.Button(screen,text="9",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("9"))
button9.grid(row=3,column= 2)
buttonC = tkinter.Button(screen,text="C",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= reset)
buttonC.grid(row=4,column= 0)
button0 = tkinter.Button(screen,text="0",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("0"))
button0.grid(row=4,column= 1)
buttonDot = tkinter.Button(screen,text=".",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("."))
buttonDot.grid(row=4,column= 2)
buttonEqual = tkinter.Button(screen,text="=",height=2,width= 42,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= calculate)
buttonEqual.grid(row=5,column= 0,columnspan= 4)
buttonX = tkinter.Button(screen,text="*",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("*"))
buttonX.grid(row=1,column= 3)
buttonPlus = tkinter.Button(screen,text="+",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("+"))
buttonPlus.grid(row=2,column= 3)
buttonMinus = tkinter.Button(screen,text="-",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("-"))
buttonMinus.grid(row=3,column= 3)
buttonDivide = tkinter.Button(screen,text="/",height=2,width= 10,bg= 'black',fg= "white",font= ("aerial",15,"bold"),command= lambda: add("/"))
buttonDivide.grid(row=4,column= 3)
screen.mainloop()