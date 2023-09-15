from tkinter import *

def button_press(num):
    
    global equations_tex

    equations_tex = equations_tex + str(num)

    equations_label.set(equations_tex)



def equals():
    
    global equations_tex
    
    try:
        total = str(eval(equations_tex))

        equations_label.set(total)

        equations_tex = total
    
    except ZeroDivisionError:

        equations_label.set("Intenta nuevamente")
    
        equations_tex = ""

    except SyntaxError:

        equations_label.set("SyntaxError")
    
        equations_tex = ""
    
    


def clear():
    
    global equations_tex

    equations_label.set("")

    equations_tex = ""



Windows = Tk()
Windows.title("Calculator Program")
Windows.geometry("500x500")

equations_tex = ""

equations_label = StringVar()

label = Label(Windows, textvariable=equations_label, font=('consolas',20), bg="White", width=24, height=2)
label.pack()

frame = Frame(Windows)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command= lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command= lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command= lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command= lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command= lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command= lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command= lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command= lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command= lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command= lambda: button_press(0))

button0.grid(row=3, column=1)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command= lambda: button_press('+'))

plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command= lambda: button_press('-'))

minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command= lambda: button_press('*'))

multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command= lambda: button_press('/'))

divide.grid(row=3, column=3)

Equals = Button(frame, text='=', height=4, width=9, font=35,
                 command= lambda: equals())

Equals.grid(row=3, column=0)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command= lambda: button_press('.'))

decimal.grid(row=3, column=2)

clear = Button(Windows, text='Clear', height=4, width=12, font=35,
                 command= clear)

clear.pack()


Windows.mainloop()
