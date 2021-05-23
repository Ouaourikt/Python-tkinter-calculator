# //////////////////////////////////////////////////////////////#
from tkinter import *
from tkinter import ttk
from tkinter import Tk

window = Tk()
style = ttk.Style(window)
style.theme_use("classic")
window.title("simple calculatr by: Ouaourikt Abdelghani")

text = StringVar()

e1 = Entry(window, width=40, borderwidth=15,textvariable=text)
e1.grid(row=0 ,column=0,columnspan=3, padx =10 , pady=10)

exp =""
def calulater_btn(value):
    global exp
    exp += str(value)
    text.set(value)

def botton_clear():
    global  exp
    exp =""
    text.set(exp)

def equale():
    global exp
    id = str(eval(exp))
    text.set(id)

btn1 = Button(window, text="1",padx=40 , pady=20 , command=lambda: calulater_btn(1) , bg="#fff" )
btn2 = Button(window, text="2",padx=40 , pady=20 , command=lambda: calulater_btn(2) , bg="#fff")
btn3 = Button(window, text="3",padx=40 , pady=20 , command=lambda: calulater_btn(3) , bg="#fff")
btn4 = Button(window, text="4",padx=40 , pady=20 , command=lambda: calulater_btn(4) , bg="#fff")
btn5 = Button(window, text="5",padx=40 , pady=20 , command=lambda: calulater_btn(5) , bg="#fff")
btn6 = Button(window, text="6",padx=40 , pady=20 , command=lambda: calulater_btn(6) , bg="#fff")
btn7 = Button(window, text="7",padx=40 , pady=20 , command=lambda: calulater_btn(7) , bg="#fff")
btn8 = Button(window, text="8",padx=40 , pady=20 , command=lambda: calulater_btn(8) , bg="#fff")
btn9 = Button(window, text="9",padx=40 , pady=20 , command=lambda: calulater_btn(9) , bg="#fff")
btn0 = Button(window, text="0",padx=40 , pady=20 , command=lambda: calulater_btn(0) , bg="#fff")

btn_plus = Button(window, text="+",padx=37 , pady=20 , command=lambda: calulater_btn("+"), bg="orange", fg="#fff",font=78)
btn_v = Button(window, text=",",padx=39 , pady=20 , command= lambda:calulater_btn(","), bg="orange", fg="#fff",font=78)
bt_p = Button(window, text="x",padx=40 , pady=20 , command=lambda: calulater_btn("*"), bg="orange", fg="#fff",font=78)
bt_c = Button(window, text="/",padx=40 , pady=20 , command=lambda: calulater_btn("/"), bg="orange", fg="#fff",font=78)
btn_m = Button(window, text="-",padx=38 , pady=20 , command=lambda: calulater_btn("-"), bg="orange", fg="#fff",font=78)
btn_egale = Button(window, text="=",padx=87 ,command=lambda: equale(),pady=20 ,bg="green", fg="#fff",font=78)
btn_clear = Button(window, text="clear",padx=28 , pady=20,command=lambda: botton_clear() ,font=78,bg="yellow", fg="#fff")
btn_cc = Button(window, text="C",padx=40 , pady=20 , command= lambda:calulater_btn("c"),font=78,bg="blue", fg="#fff")

btn1.grid(row="4",column="0")
btn2.grid(row="4" ,column="1")
btn3.grid(row="4" ,column="2")

btn4.grid(row="3" ,column="0")
btn5.grid(row="3" ,column="1")
btn6.grid(row="3" ,column="2")

btn7.grid(row="2" ,column="0")
btn8.grid(row="2" ,column="1")
btn9.grid(row="2" ,column="2")

btn0.grid(row="6" ,column="0")

btn_cc.grid(row="1", column="0", columnspan=1)
btn_m.grid(row="3", column="3",columnspan=2)
btn_v.grid(row="4",column="3",columnspan=2)
btn_plus.grid(row="2" , column="3",columnspan=2)
btn_egale.grid(row="6" , column="1",columnspan=2)
btn_clear.grid(row="1" , column="3",columnspan=2)
bt_p.grid(row="1", column="2",columnspan=1)
bt_c.grid(row="1", column="1",columnspan=1)

window.mainloop()