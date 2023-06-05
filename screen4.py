from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=3)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=3)
Label(root,text='Bus Ticket').grid(row=3,column=3,columnspan=3)
'''showinfo('success','Seat Booked.....') '''




root.mainloop()
