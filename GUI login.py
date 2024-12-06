import tkinter as A 

form=A.Tk()
form.geometry("550x700")
form.title("Registration Form")

head=A.Label(form,text="Registration Form",fg="red",font=('bold',25),justify="center")
head.place(x=150,y=10)

DataOne=A.StringVar()
DataTwo=A.StringVar()
DataThree=A.StringVar()
DataFour=A.StringVar()
DataFour.set("none")
DataFive=A.StringVar()
DataFive.set("none")
DataSix=A.StringVar()
DataSix.set("none")
DataSeven=A.StringVar()
DataSeven.set("none")
click=A.StringVar()
click.set("Enter your state")

def submit():
 	Name=DataOne.get()
 	print("Username:",Name)
 	email=DataTwo.get()
 	print("Email:",email)
 	psw=DataThree.get()
 	print("Password:",psw)
 	gen=DataFour.get()
 	print("Gender:",gen)
 	state=click.get()
 	print("State",state)
 	py=DataFive.get()
 	print("Python:",py)
 	java=DataSix.get()
 	print("Java:",java)
 	C=DataSeven.get()
 	print("C++",C)
 	

 			#Username
box1=A.Label(form,text="Name",font=('bold',15))
box1.place(x=30,y=70)
box1Entry=A.Entry(form,textvariable=DataOne,width=20,font=('bold',15))
box1Entry.place(x=150,y=60)



			#Email
box2=A.Label(form,text="Email",font=('bold',15))
box2.place(x=30,y=110)
box2Entry=A.Entry(form,textvariable=DataTwo,width=20,font=('bold',15))
box2Entry.place(x=150,y=110)



			#Password
psw=A.Label(form,text="Password",font=('bold',15))
psw.place(x=30,y=150)
box3Entry=A.Entry(form,textvariable=DataThree,width=20,show="X",font=('bold',15))
box3Entry.place(x=150,y=150)



			#Gender
box3=A.Label(form,text="Gender",font=('bold',15))
box3.place(x=30,y=190)
male=A.Radiobutton(text="Male",value="male",variable=DataFour,font=('bold',10))
male.place(x=160,y=190)
female=A.Radiobutton(text="Female",value="female",variable=DataFour,font=('bold',10))
female.place(x=220,y=190)



			#State
box4=A.Label(form,text="State",font=('bold',15))
box4.place(x=30,y=230)
drop=A.OptionMenu(form,click,"Delhi","Mumbai","Agra")
drop.place(x=190,y=230)





			#Programming
box4=A.Label(form,text="Programming",font=('bold',15))
box4.place(x=30,y=270)
chck=A.Checkbutton(text="Python",onvalue="Yes",offvalue="No",variable=DataFive,font=('bold',10))
chck.place(x=160,y=270)
chck2=A.Checkbutton(text="Java",onvalue="Yes",offvalue="No",variable=DataSix,font=('bold',10))
chck2.place(x=230,y=270)
chck3=A.Checkbutton(text="C++",onvalue="Yes",offvalue="No",variable=DataSeven,font=('bold',10))
chck3.place(x=300,y=270)



			#Submit Button
btn=A.Button(form,text="Submit",bg="blue",fg="white",command=submit,font=("bold",20))
btn.place(x=10,y=400)

form.mainloop()