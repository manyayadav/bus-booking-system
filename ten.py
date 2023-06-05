from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=4)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=4)
Label(root,text='Add Bus Running Details',font='Arial 14 bold',bg='grey97',fg='dark green').grid(row=3,column=3,pady=20,columnspan=4)
Label(root,text='Bus ID').grid(row=4,column=0)
Entry(root,font='Arial 14 bold').grid(row=4,column=1)
Label(root,text='Running Date').grid(row=4,column=2)
Entry(root,font='Arial 14 bold').grid(row=4,column=3)
Label(root,text='Seat Available').grid(row=4,column=4)
Entry(root,font='Arial 14 bold').grid(row=4,column=5)
Button(root,text='Add Run',bg='light green',fg='dark green',font='Arial 14').grid(row=4,column=6,padx=15)
Button(root,text='Delete Run',bg='light green',fg='red',font='Arial 14').grid(row=4,column=7)
immg=PhotoImage(file="home.png")
Button(root,image=immg).grid(row=5,column=6)



root.mainloop()
