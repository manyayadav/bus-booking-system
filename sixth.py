from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=1,columnspan=4)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=1,pady=15,columnspan=4)
Label(root,text='Add New Details to DataBase',bg='grey99',fg='green').grid(row=3,column=1,columnspan=4,pady=20)
Button(root,text='New Operator',bg='light green',fg='black').grid(row=4,column=1,padx=20)
Button(root,text='New Bus',bg='tomato2',fg='black').grid(row=4,column=2,padx=20)
Button(root,text='New Route',bg='steel blue',fg='black').grid(row=4,column=3,padx=20)
Button(root,text='New Run',bg='lightsalmon3',fg='black').grid(row=4,column=4)


root.mainloop()
