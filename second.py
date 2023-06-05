from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=1)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red').grid(row=2,column=1)
Button(root,text='Seat booking',bg='light green',fg='black').grid(row=3,column=0)
Button(root,text='Check booked seat',bg='green',fg='black').grid(row=3,column=1)
Button(root,text='Add bus details',bg='dark green',fg='black').grid(row=3,column=2)
Label(root,text='For admins online',fg='red').grid(row=5,column=2)




root.mainloop()
