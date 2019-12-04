# import everything from tkinter module 
import tkinter
from tkinter import *
import math

# globally declare the expression variable
expression = ""


# Function to update expressiom
# in the text entry box 
def press(num):
    # point out the global expression variable
    global expression

    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


def sqrt():
    global expression
    exp = math.sqrt(float(expression))
    equation.set(exp)
    return exp


def delete():
    global expression

    expression = expression[:-1]
    equation.set(expression)


def factor():
    global expression
    exp = math.factorial(float(expression))
    equation.set(exp)
    return exp


def power(a, b):
    global expression
    exp = math.pow(float(a), float(b))
    equation.set(exp)
    return exp

def sinus():
    global expression

    exp = math.sin(float(expression) * math.pi / 180)
    if exp==1.2246467991473532e-16 or exp==-2.4492935982947064e-16:
        equation.set(round(exp))
        return round(exp)
    else:
        equation.set(exp)
        return exp


def cosinus():
    global expression
    exp = math.cos(float(expression) * math.pi / 180)
    if exp == 6.123233995736766e-17 or exp == -1.8369701987210297e-16:
        equation.set(round(exp))
        return round(exp)
    else:
        equation.set(exp)
        return exp


def logar():
    global expression
    if float(expression)==0:
        equation.set("undefined")
    else:

        exp = math.log(float(expression), 10)
        equation.set(exp)


def numpi():
    global expression
    expression = str(math.pi)
    equation.set(expression)


def percent(a, b):
    global expression

    exp = float(a) / 100 * float(b)
    equation.set(exp)
    return exp


# Function to evaluate the final expression 
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    global expression
    global total
    # Put that code inside the try block
    # which may generate the error
    if "^" in expression:

        temp = expression.split("^")
        a = temp[0]
        b = temp[1]
        total = str(power(a, b))
        expression = ""

    elif "%" in expression:

        temp = expression.split("%")
        a = temp[0]
        b = temp[1]
        total = str(percent(a, b))
        expression = ""

    elif "!" in expression:
        temp = expression.split("!")
        expression = temp[0]
        total = str(factor())
        expression = total


    else:
        try:

            # eval function evaluate the expression
            # and str function convert the result
            # into string
            total = str(eval(expression))

            equation.set(total)

            # initialze the expression variable
            # by empty string
            expression = ""

        # if error is generate then handle
        # by the except block
        except:

            equation.set(" error ")
            expression = ""


def ans():
    global expression
    global total

    if expression is "":
        expression = total
        equation.set(expression)

    else:
        expression = expression + str(total)
        equation.set(expression)


# Function to clear the contents
# of text entry box 
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code 
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="black")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("430x460")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    gui.iconbitmap('Cal.ico')
    expression_field = Entry(gui, font=("Courier New", 16, 'bold'), textvariable=equation, width=10, bd=30,
                             justify='right', state='readonly')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=10, ipadx=115)

but0 = Button(gui, padx=46, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10, y=380)

but1 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=10, y=310)

but2 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=75, y=310)

but3 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=140, y=310)

but4 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=10, y=240)

but5 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75, y=240)

but6 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=140, y=240)

but7 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=10, y=170)

but8 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=75, y=170)

but9 = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=140, y=170)

butdot = Button(gui, padx=14, pady=14, bd=4, bg='gray40', fg='white', command=lambda: press(","), text=",",
                font=("Courier New", 16, 'bold'))
butdot.place(x=140, y=380)

butpl = Button(gui, padx=14, pady=14, bd=4, bg='chocolate2', fg='white', text="+", command=lambda: press("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(gui, padx=14, pady=14, bd=4, bg='chocolate2', fg='white', text="-", command=lambda: press("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butml = Button(gui, padx=14, pady=14, bd=4, bg='chocolate2', fg='white', text="*", command=lambda: press("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=205, y=240)

butdiv = Button(gui, padx=14, pady=14, bd=4, bg='chocolate2', fg='white', text="/", command=lambda: press("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)

butclear = Button(gui, padx=8, pady=14, bd=4, bg='light gray', text="CE", command=clear,
                  font=("Courier New", 16, 'bold'))
butclear.place(x=10, y=100)

butperc = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="%", command=lambda: press("%"),
                 font=("Courier New", 16, 'bold'))
butperc.place(x=75, y=100)

butequal = Button(gui, padx=14, pady=14, bd=4, bg='chocolate2', fg='white' , command=equalpress, text="=",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=205, y=380)

bra1 = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="(", command=lambda: press("("),
              font=("Courier New", 16, 'bold'))
bra1.place(x=270, y=100)

bra2 = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text=")", command=lambda: press(")"),
              font=("Courier New", 16, 'bold'))
bra2.place(x=270, y=170)

pwr = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="^", command=lambda: press("^"),
             font=("Courier New", 16, 'bold'))
pwr.place(x=270, y=380)

fac = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="!", command=lambda: press("!"), font=("Courier New", 16, 'bold'))
fac.place(x=140, y=100)

root = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text='√', command=sqrt, font=("Courier New", 16, 'bold'))
root.place(x=270, y=240)

npi = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text='π', command=numpi, font=("Courier New", 16, 'bold'))
npi.place(x=270, y=310)

sinus = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="sin", command=sinus,
               font=("Courier New", 16, 'bold'))
sinus.place(x=335, y=100)

cosinus = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="cos", command=cosinus,
                 font=("Courier New", 16, 'bold'))
cosinus.place(x=335, y=170)

logar = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="log", command=logar,
               font=("Courier New", 16, 'bold'))
logar.place(x=335, y=240)

dellast = Button(gui, padx=7, pady=14, bd=4, bg='light gray', text="<---", command=delete,
                 font=("Courier New", 16, 'bold'))
dellast.place(x=335, y=310)

ans = Button(gui, padx=14, pady=14, bd=4, bg='light gray', text="ans", command=ans, font=("Courier New", 16, 'bold'))
ans.place(x=335, y=380)

gui.mainloop()
