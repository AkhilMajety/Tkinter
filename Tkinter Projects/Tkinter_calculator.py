from tkinter import*


me = Tk()
me.title("Simple Calculator")

e = Entry(me,width = 35,borderwidth=5)
e.grid(row = 0,column = 0,columnspan = 3,padx=10,pady=10)



def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_add():
	first_number = e.get()
	global f_num 
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)

def button_equal():
	second_number = e.get()
	e.delete(0,END)

	if math == "addition":
		e.insert(0,f_num + int(second_number))

	if math == "subtraction":
		e.insert(0,f_num - int(second_number))

	if math == "multiplication":
		e.insert(0,f_num * int(second_number))


	if math == "division":
		e.insert(0,f_num / int(second_number))


def button_multiply():
	first_number = e.get()
	global f_num 
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_division():
	first_number = e.get()
	global f_num 
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0,END)
	return

def button_subtract():
	first_number = e.get()
	global f_num 
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0,END)
	return


b_1 = Button(me,text='1',padx = 40,pady=20,command = lambda :button_click(1))
b_2 = Button(me,text='2',padx = 40,pady=20,command = lambda :button_click(2))
b_3 = Button(me,text='3',padx = 40,pady=20,command = lambda :button_click(3))
b_4 = Button(me,text='4',padx = 40,pady=20,command = lambda :button_click(4))
b_5 = Button(me,text='5',padx = 40,pady=20,command = lambda :button_click(5))
b_6 = Button(me,text='6',padx = 40,pady=20,command = lambda :button_click(6))
b_7 = Button(me,text='7',padx = 40,pady=20,command = lambda :button_click(7))
b_8 = Button(me,text='8',padx = 40,pady=20,command = lambda :button_click(8))
b_9 = Button(me,text='9',padx = 40,pady=20,command = lambda :button_click(9))
b_0 = Button(me,text='0',padx = 40,pady=20,command = lambda :button_click(0))


button_add = Button(me,text='+',padx = 39,pady=20,command = button_add)
button_clear = Button(me,text='Clear',padx = 79,pady=20,command = button_clear)
button_equal =  Button(me,text='=',padx = 91,pady=20,command =button_equal)


button_subtract = Button(me,text='-',padx = 41,pady=20,command = button_subtract)

button_multiply = Button(me,text='*',padx = 40,pady=20,command = button_multiply)

button_division = Button(me,text='/',padx = 41	,pady=20,command = button_division)

b_1.grid(row = 3 ,column = 0 )
b_2.grid(row = 3 , column = 1)
b_3.grid(row = 3 , column = 2)

b_4.grid(row = 2 , column =0 )
b_5.grid(row = 2, column = 1 )
b_6.grid(row = 2 , column =2 )

b_7.grid(row = 1 , column =0 )
b_8.grid(row = 1, column = 1 )
b_9.grid(row = 1 , column =2 )


b_0.grid(row = 4 , column =0 )


button_add.grid(row = 5 , column =0)
button_clear.grid(row = 4 , column =1,columnspan=2)
button_equal.grid(row = 5 , column =1 ,columnspan=2)



button_subtract.grid(row = 6 , column =0)
button_multiply.grid(row = 6 , column =1)
button_division.grid(row = 6 , column =2)

me.mainloop()


