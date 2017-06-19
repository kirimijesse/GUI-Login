from tkinter import *
import os
 
creds = 'tempfile.temp'

def Signup():


	roots = Tk()
	roots.title('Signup')
	instruction = Label(roots, text='Please Enter new Credentials')
	instruction.grid(row=0, column=0, sticky=E)

	name = Label(roots, text='New Username: ')
	pwordL = Label(roots,text='New Password: ')
	nameL.grid(row=1, column=0, sticky=W)

	nameE = Entry = Entry(roots)
	pwordE = Entry(roots, show='*')

	signupButton = Button(roots, text='Signup', command=FSSignup)
	signupButton.grid(columnspan=2, sticky=W)
	roots.mainloop()

def FFSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())	
		f.write('\n')
		f.write(pwordE.get())
		f.close()

	roots.destroy()
	Login()

def Login():

	rootA = Tk()
	rootA.title('Login')

	instruction = Label(rootA, text='Please Login\n')
	instruction.grid(sticky=E)

	nameL = Label(rootA, text='Username: ')
	pwordL = Label(rootA, text='Password: ')
	nameL.grid(row=1, sticky=W)
	pwordL.grid(row2=2, sticky=W)

	nameEL = Entry(rootA)
	pwordEL = Entry(rootA, show='*')
	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)

	loginB = Button(rootA, text='Delete User', fg='red', command=DelUser)
	rmuser.grid