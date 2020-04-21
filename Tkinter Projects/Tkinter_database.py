from tkinter import *
import sqlite3

root = Tk()
root.title('hello')
#root.iconbitmap('C:/Users/Lenovo/Desktop/1.ico')
#root.geometry("400x400")
#create table
'''
\


c.execute("""CREATE TABLE addresses(
 	first_name text,
 	last_name text,
 	address text,
 	zipcode integer

 	)""")


'''
def submit():

	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()
	c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address, :zipcode)",
			{
				'f_name' : f_name.get(),

		        'l_name' : l_name.get(),

		        'address' : address.get(),

		        'zipcode' : zipcode.get()



			}




		)

	conn.commit()



	conn.close()




	f_name.delete(0,END)

	l_name.delete(0,END)

	address.delete(0,END)

	zipcode.delete(0,END)





def query():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()




	c.execute("SELECT *,oid FROM addresses")
	records = c.fetchall()
	#print(records)

	print_records=''
	for record in records:
		print_records += str(record[0])+ " "+ str(record[1])+" " + "\t"+ str(record[4])+ "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=11,column=0,columnspan=2)


	conn.commit()



	conn.close()



	return
def delete():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()

	c.execute("DELETE from addresses WHERE oid="+delete_box.get())


	conn.commit()



	conn.close()




	



def update():

	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()
	record_id = delete_box.get()


	c.execute("""UPDATE addresses SET

		first_name=  :first,
		last_name = :last,
		address = :address,
		zipcode = :zipcode

		WHERE oid = :oid""",
		{	
			'first':f_name.get(),
			'last':l_name.get(),
			'address':address.get(),
			'zipcode':zipcode.get(),
			'oid':record_id


		}
		)

	

	conn.commit()



	conn.close()
	editor.destroy()

	




def edit():
	global editorś
	editor = Tk()
	editor.title('Update a Record')


	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()



	record_id = delete_box.get()
	c.execute("SELECT *FROM addresses WHERE oid=" + record_id)
	records = c.fetchall()

	


	


	conn.commit()



	conn.close()


	
	global f_name
	global l_name
	global address
	global zipcode

	f_name = Entry(editor,width = 30)
	f_name.grid(row= 0,column=1,padx=20,pady=(10,0))

	l_name = Entry(editor,width = 30)
	l_name.grid(row= 1,column=1)

	address = Entry(editor,width = 30)
	address.grid(row= 2,column=1)

	zipcode = Entry(editor,width = 30)
	zipcode.grid(row= 3,column=1)

	


	f_name_label = Label(editor,text = "First Name")
	f_name_label.grid(row = 0,column = 0)


	l_name_label = Label(editor,text = "Last Name")
	l_name_label.grid(row = 1,column = 0)

	address_label = Label(editor,text = "Address")
	address_label.grid(row = 2,column = 0)

	zipcode_label = Label(editor,text = "zipcode")
	zipcode_label.grid(row = 3,column = 0)

	edit_btn = Button(editor,text='Save Records',command = update)
	edit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=145)




	for record in records:
		f_name.insert(0,record[0])

		l_name.insert(0,record[1])

		address.insert(0,record[2])

		zipcode.insert(0,record[3])


	editor.mainloop


 




f_name = Entry(root,width = 30)
f_name.grid(row= 0,column=1,padx=20,pady=(10,0))

l_name = Entry(root,width = 30)
l_name.grid(row= 1,column=1)

address = Entry(root,width = 30)
address.grid(row= 2,column=1)

zipcode = Entry(root,width = 30)
zipcode.grid(row= 3,column=1)


delete_box = Entry(root,width = 30)
delete_box.grid(row= 9,column=1)

f_name_label = Label(root,text = "First Name")
f_name_label.grid(row = 0,column = 0)


l_name_label = Label(root,text = "Last Name")
l_name_label.grid(row = 1,column = 0)

address_label = Label(root,text = "Address")
address_label.grid(row = 2,column = 0)

zipcode_label = Label(root,text = "zipcode")
zipcode_label.grid(row = 3,column = 0)


delete_box_label = Label(root,text = "Select ID")
delete_box_label.grid(row = 9,column = 0)

#buttons
submit_button = Button(root,text = "Add record to DB",command = submit)
submit_button.grid(row=6,column=0,columnspan = 2,padx=10,pady=10,ipadx=100)


query_btn = Button(root,text='Show Records',command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

  

delete_btn = Button(root,text='Delete Records',command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=137)



edit_btn = Button(root,text='Edit Records',command=edit)
edit_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=145)

root.mainloop()

 