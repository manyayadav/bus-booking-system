from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=3)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=3)
Label(root,text='Entry Journey Details',bg='light green',fg='dark green').grid(row=3,column=3,columnspan=3)
Label(root,text='To',fg='black').grid(row=4,column=0,padx=0)
Entry(root,font='Arial 14 bold',fg='black').grid(row=4,column=1)
Label(root,text='From',fg='black').grid(row=4,column=2)
Entry(root,font='Arial 14 bold',fg='black').grid(row=4,column=3)
Label(root,text='Journey date',fg='black').grid(row=4,column=4)
Entry(root,font='Arial 14 bold',fg='black').grid(row=4,column=5)
Button(root,text='Show Bus',bg='green',fg='black').grid(row=4,column=6)
immg=PhotoImage(file="home.png")
Button(root,image=immg).grid(row=4,column=7)
'''Label(root,text='Select bus',fg='green').grid(row=5,column=0)
Label(root,text='operator',fg='green').grid(row=5,column=1)
Label(root,text='Bus Type',fg='green').grid(row=5,column=2)
Label(root,text='Available Capacity',fg='green').grid(row=5,column=3)
Label(root,text='Fare',fg='green').grid(row=5,column=4,pady=16)
Button(root,text='Bus 1',bg='light blue').grid(row=6,column=0)
Label(root,text='Kamla',fg='blue').grid(row=6,column=1)
Label(root,text='AC 2X2',fg='blue').grid(row=6,column=2)
Label(root,text='',fg='blue').grid(row=6,column=3)
Button(root,text='Proceed to Book',bg='green').grid(row=6,column=6)'''
Label(root,text='Fill Passanger Details to book the bus ticket',font='Arial 14 bold',bg='light blue',fg='red').grid(row=7,column=3,pady=15,columnspan=3)
Label(root,text='Name',fg='black').grid(row=8,column=0)
Entry(root,font='Arial 14 bold',fg='black').grid(row=8,column=1)
Label(root,text='Gender',fg='black').grid(row=8,column=2)
gender_type=StringVar()
opt=['male','female','other']
d_menu=OptionMenu(root,gender_type,*opt).grid(row=8,column=3)

Label(root,text='No of seats',fg='black').grid(row=8,column=4)
Entry(root,font='Arial 14 bold',fg='black').grid(row=8,column=5)
Label(root,text='Mobile No',fg='black').grid(row=8,column=6)
Entry(root,font='Arial 14 bold',fg='black').grid(row=8,column=7)
Label(root,text='Age',fg='black').grid(row=8,column=8)
Entry(root,font='Arial 14 bold',fg='black').grid(row=8,column=9)
Button(root,text='Book seat',bg='green').grid(row=8,column=10)







root.mainloop()
