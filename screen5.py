from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=3,columnspan=3)
Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=2,column=3,pady=15,columnspan=3)
Label(root,text='Check your Booking',font='Arial 14 bold',bg='light green',fg='dark green').grid(row=3,column=3,pady=15,columnspan=3)
Label(root,text='Enter your Mobile No:').grid(row=4,column=3)
Entry(root,font='Arial 14 bold').grid(row=4,column=4)
Button(root,text='Check Booking').grid(row=4,column=5)
'''askyesno('No Booking Record','Do you want book seat now?')'''


root.mainloop()
