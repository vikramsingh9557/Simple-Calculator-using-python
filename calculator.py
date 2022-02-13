from tkinter import *
root = Tk()
# Driver code
if __name__ == "__main__":
	

	# set the background colour of GUI window
	root.configure(background="light green")

	# set the title of GUI window
	root.title("Simple Calculator")

	# set the configuration of GUI window
	root.geometry("270x150")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	
equa = ""
equation = StringVar()
calculation = Label(root,textvariable = equation)
equation.set("Enter your equation:")
calculation.grid(columnspan = 4)


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def Clear():
    global equa
    equation.set("")
    equa = ""

Button0 = Button(root, text="0",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(0),height=1, width=7)
Button0.grid(row = 4,column = 1)
Button1 = Button(root, text="1",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(1),height=1, width=7)
Button1.grid(row = 1,column = 0)
Button2 = Button(root, text="2",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(2),height=1, width=7)
Button2.grid(row = 1,column = 1)
Button3 = Button(root, text="3",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(3),height=1, width=7)
Button3.grid(row = 1,column = 2)
Button4 = Button(root, text="4",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(4),height=1, width=7)
Button4.grid(row = 2,column = 0)
Button5 = Button(root, text="5",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(5),height=1, width=7)
Button5.grid(row = 2,column = 1)
Button6 = Button(root, text="6",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(6),height=1, width=7)
Button6.grid(row = 2,column = 2)
Button7 = Button(root, text="7",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(7),height=1, width=7)
Button7.grid(row = 3,column = 0)
Button8 = Button(root, text="8",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(8),height=1, width=7)
Button8.grid(row = 3,column = 1)
Button9 = Button(root, text="9",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress(9),height=1, width=7)
Button9.grid(row = 3,column = 2)
Equal= Button(root, text="=",relief = 'ridge', activebackground='orange',activeforeground='white',command = EqualPress,height=1, width=7)
Equal.grid(row = 4,column = 0 )
Clear = Button(root, text="C",relief = 'ridge', activebackground='orange',activeforeground='white',command = Clear,height=1, width=7)
Clear.grid(row = 4,column = 2)
Addition = Button(root, text="+",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress("+"),height=1, width=7)
Addition.grid(row = 1,column = 3)
Subtraction = Button(root, text="-",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress("-"),height=1, width=7)
Subtraction.grid(row = 2,column = 3)
Multiply = Button(root, text="*",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress("*"),height=1, width=7)
Multiply.grid(row = 3,column = 3)
Division= Button(root, text="/",relief = 'ridge', activebackground='orange',activeforeground='white',command = lambda:btnPress("/"),height=1, width=7)
Division.grid(row = 4,column = 3)

root.mainloop()
