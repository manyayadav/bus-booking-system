from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=6)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=6)
Label(root,text='Add Bus  Details',font='Arial 14 bold',bg='grey97',fg='dark green').grid(row=3,column=3,pady=20,columnspan=6)
Label(root,text='Bus id').grid(row=4,column=0)
Entry(root,font='Arial 14 bold').grid(row=4,column=1)
Label(root,text='Bus Type').grid(row=4,column=2)
bus_type=StringVar()
bus_type.set('Bus Type')
opt=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC-Sleeper 2X1']
d_menu=OptionMenu(root,bus_type,*opt).grid(row=4,column=3)
Label(root,text='Capacity').grid(row=4,column=4)
Entry(root,font='Arial 14 bold').grid(row=4,column=5)
Label(root,text='Fare RS').grid(row=4,column=6)
Entry(root,font='Arial 14 bold').grid(row=4,column=7)
Label(root,text='Operator ID').grid(row=4,column=8)
Entry(root,font='Arial 14 bold').grid(row=4,column=9)
Label(root,text='Route id').grid(row=4,column=10)
Entry(root,font='Arial 14 bold').grid(row=4,column=11,pady=39)
Button(root,text='Add bus',bg='light green',fg='dark green',font='Arial 14').grid(row=5,column=6)
Button(root,text='Edit bus',bg='light green',fg='dark green',font='Arial 14').grid(row=5,column=7)
immg=PhotoImage(file="home.png")
Button(root,image=immg).grid(row=5,column=8)

root.mainloop()

