from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=4)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=4)
Label(root,text='Add Bus Route Details',font='Arial 14 bold',bg='grey97',fg='dark green').grid(row=3,column=3,pady=20,columnspan=4)
Label(root,text='Route id').grid(row=4,column=0)
Entry(root,font='Arial 14 bold').grid(row=4,column=1)
Label(root,text='Station Name').grid(row=4,column=2)
Entry(root,font='Arial 14 bold').grid(row=4,column=3)
Label(root,text='Station id').grid(row=4,column=4)
Entry(root,font='Arial 14 bold').grid(row=4,column=5)
Button(root,text='Add Route',bg='light green',fg='dark green',font='Arial 14').grid(row=4,column=7,padx=15)
Button(root,text='Delete Route',bg='light green',fg='red',font='Arial 14').grid(row=4,column=8)
immg=PhotoImage(file="home.png")
Button(root,image=immg).grid(row=5,column=6)



root.mainloop()
