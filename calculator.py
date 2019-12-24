from tkinter import *

expression=""


def press(num):
	global expression	
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:
		equation.set("Error")
		expression=""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	root = Tk()
	root.geometry("300x185+500+300")
	root.resizable(False,False)
	root.title("Simple Calculator")


	equation = StringVar()

	expression_field = Entry(root, textvariable=equation)
	expression_field.grid(columnspan=6, ipadx=90)


	btn1=Button(root,text="1",fg="white", bg="black",
		    command=lambda: press(1),height=2, width=9)
	btn1.grid(row=2,column=0)

	btn2=Button(root,text="2",fg="white", bg="black",
		   command=lambda: press(2), height=2, width=9)
	btn2.grid(row=2,column=1)

	btn3=Button(root,text="3",fg="white", bg="black",
		   command=lambda: press(3), height=2, width=9)	
	btn3.grid(row=2,column=2)
	
	btn4=Button(root,text="4",fg="white", bg="black",
		  command=lambda: press(4), height=2, width=9)
	btn4.grid(row=3,column=0)

	btn5=Button(root,text="5",fg="white", bg="black",
		   command=lambda: press(5), height=2, width=9)
	btn5.grid(row=3,column=1)
	
	btn6=Button(root,text="6",fg="white", bg="black",
		   command=lambda: press(6), height=2, width=9)
	btn6.grid(row=3,column=2)
	
	btn7=Button(root,text="7",fg="white", bg="black",
		   command=lambda: press(7), height=2, width=9)
	btn7.grid(row=4,column=0)

	btn8=Button(root,text="8",fg="white", bg="black",
		   command=lambda: press(8), height=2, width=9)
	btn8.grid(row=4,column=1)

	btn9=Button(root,text="9",fg="white", bg="black",
		   command=lambda: press(9), height=2, width=9)
	btn9.grid(row=4,column=2)

	btn0=Button(root,text="0",fg="white", bg="black",
		    height=2, width=9)
	btn0.grid(row=5,column=0)
	
	btnAdd=Button(root,text="+",fg="white", bg="black",
		   command=lambda: press("+"), height=2, width=9)
	btnAdd.grid(row=2,column=3)

	btnSub=Button(root,text="-",fg="white", bg="black",
		    command=lambda: press("-"),height=2, width=9)
	btnSub.grid(row=3,column=3)
	
	btnMul=Button(root,text="*",fg="white", bg="black",
		   command=lambda: press("*"), height=2, width=9)
	btnMul.grid(row=4,column=3)
	
	btnDiv=Button(root,text="/",fg="white", bg="black",
		   command=lambda: press("/"), height=2, width=9)
	btnDiv.grid(row=5,column=3)
	
	btnClear=Button(root,text="AC",fg="white", bg="black",
		    command=clear, height=2, width=9)
	btnClear.grid(row=5,column=1)

	btnEqual=Button(root,text="=",fg="white", bg="black",
		   command=equalpress, height=2, width=9)
	btnEqual.grid(row=5,column=2)
	
	
	root.mainloop()