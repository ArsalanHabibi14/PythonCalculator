from tkinter import *

strNumber = ""


def press(num):
    global strNumber
    strNumber = strNumber + str(num)
    Number.set(strNumber)


def equal():
    try:
        global strNumber

        total = str(eval(strNumber))
        Number.set(total)

        strNumber = ''

    except:
        Number.set(' error ')
        strNumber = ''


def clear():
    global strNumber
    strNumber = ""
    Number.set("0")


# ====================== Settings ====================
window = Tk()
window.title("Calculator")
window.geometry("410x500")
Number = StringVar()
# ========================== entry ===============
mainEntry = Entry(window, width=65, textvariable=Number)
mainEntry.place(x=10, y=20, height=50)
# ========================= buttons ===================
b1 = Button(window, text="1", width=12, height=6, command=lambda: press(1))
b1.place(x=4, y=75)

b2 = Button(window, text="2", width=12, height=6, command=lambda: press(2))
b2.place(x=100, y=75)

b3 = Button(window, text="3", width=12, height=6, command=lambda: press(3))
b3.place(x=195, y=75)

bdiv = Button(window, text="/", width=12, height=6, command=lambda: press("/"), bg="orange")
bdiv.place(x=290, y=75)

b4 = Button(window, text="4", width=12, height=6, command=lambda: press(4))
b4.place(x=4, y=175)

b5 = Button(window, text="5", width=12, height=6, command=lambda: press(5))
b5.place(x=100, y=175)

b6 = Button(window, text="6", width=12, height=6, command=lambda: press(6))
b6.place(x=195, y=175)

bmul = Button(window, text="*", width=12, height=6, command=lambda: press("*"), bg="orange")
bmul.place(x=290, y=175)

b7 = Button(window, text="7", width=12, height=6, command=lambda: press(7))
b7.place(x=4, y=275)

b8 = Button(window, text="8", width=12, height=6, command=lambda: press(8))
b8.place(x=100, y=275)

b9 = Button(window, text="9", width=12, height=6, command=lambda: press(9))
b9.place(x=195, y=275)

bplus = Button(window, text="+", width=12, height=6, command=lambda: press("+"), bg="orange")
bplus.place(x=290, y=275)

b0 = Button(window, text="0", width=12, height=6, command=lambda: press(0))
b0.place(x=4, y=375)

bc = Button(window, text="C", width=12, height=6, bg="orange", command=clear)
bc.place(x=100, y=375)

beq = Button(window, text="=", width=12, height=6, command=equal, bg="orange")
beq.place(x=195, y=375)

bminu = Button(window, text="-", width=12, height=6, command=lambda: press("-"), bg="orange")
bminu.place(x=290, y=375)

window.mainloop()
