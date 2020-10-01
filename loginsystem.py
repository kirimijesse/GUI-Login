from tkinter import *
import os
 
creds = 'tempfile.temp'

def Signup():
	global pwordE
	global nameE
	global roots

	roots = Tk()
	roots.title('Signup')
	instruction = Label(roots, text='Please Enter new Credentials')
	instruction.grid(row=0, column=0, sticky=E)

	nameL = Label(roots, text='New Username: ')
	pwordL = Label(roots,text='New Password: ')
	nameL.grid(row=1, column=0, sticky=W)
	pwordL.grid(row=2, column=0, sticky=W)

	nameE = Entry(roots)
	pwordE = Entry(roots, show='*')
	nameE.grid(row=1, column=1)
	pwordE.grid(row=2, column=1)

	signupButton = Button(roots, text='Signup', command=FSSignup, fg='black', bg='SeaGreen1',padx=5,pady=2)
	signupButton.grid(columnspan=2, sticky=W)
	roots.mainloop()

def FSSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())	
		f.write('\n')
		f.write(pwordE.get())
		f.close()

	roots.destroy()
	Login()

def Login():
	global nameEL
	global pwordEL
	global rootA

	rootA = Tk()
	rootA.minsize(500,500)
	rootA.title('Login')

	instruction = Label(rootA, text='Please Login\n',font=('Verdana', 12), fg='black',padx=5,pady=2)
	instruction.place(relx=0.5,rely=0.3,anchor='center')

	nameL = Label(rootA, text='Username: ')
	pwordL = Label(rootA, text='Password: ')
	nameL.place(relx=0.3,rely=0.45)
	pwordL.place(relx=0.3,rely=0.55)

	nameEL = Entry(rootA,)
	pwordEL = Entry(rootA, show='*')
	nameEL.place(relx=0.5,rely=0.45)
	pwordEL.place(relx=0.5,rely=0.55)

	loginB = Button(rootA, text='Login', command=CheckLogin,font=('Verdana', 8), fg='black', bg='SeaGreen1',padx=5,pady=2)
	loginB.place(relx=0.5,rely=0.7,anchor='center')

	rmuser = Button(rootA, text='Delete User', command=DelUser,font=('Verdana', 8), fg='black', bg='SeaGreen1',padx=5,pady=2)
	rmuser.place(relx=0.5,rely=0.85,anchor='center')
	rootA.mainloop()

def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()

	if nameEL.get() == uname and pwordEL.get() == pword:
		r = Tk()
		r.title(':D')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[+] Logged In')
		rlbl.pack()
		r.mainloop()
	else:
		r = Tk()	
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()	

def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

if os.path.isfile(creds):
	Login()
else:
	Signup()