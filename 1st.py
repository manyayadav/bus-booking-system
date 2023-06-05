from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry=('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red').grid(row=2,column=0)
Label(root,text='Name: Anushka Kushwaha',fg='blue').grid(row=3,column=0,pady=15)
Label(root,text='Er: 211B061',fg='blue').grid(row=4,column=0,pady=10)
Label(root,text='mobile: 7880021203',fg='blue').grid(row=5,column=0,pady=10)
Label(root,text='submitted to: Dr. Mahesh Kumar',bg='light blue',fg='red').grid(row=8,column=0)
Label(root,text='project based learning',fg='red').grid(row=9,column=0)





root.mainloop()
