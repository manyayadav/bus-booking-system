from tkinter import*
root=Tk()
root.geometry("1366x768")
label2=Label(root,text="  ").grid(row=0,column=0,padx=200)
label1=Label(root,text="Online Bus Booking System",font=("Aerial 30 bold"),fg="red",bg="sky blue")
pic=PhotoImage(file=".\\Bus_for_project.png")
label1.grid(row=2,column=4)
Label(root,image=pic).grid(row=0,column=4,pady=50)
Label(root,text=" Name: MANYA YADAV",fg="blue",font="Aerial 20").grid(row=5,column=4,pady=50)
Label(root,text="Er: 211B178",fg="blue",font="Aerial 20").grid(row=6,column=4)
Label(root,text="Mobile: 0987654321",fg="blue",font="Aerial 20").grid(row=9,column=4,pady=50)
Label(root,text="Submitted To:Dr. MAHESH KUMAR",font=("Aerial 30 bold"),fg="red",bg="sky blue").grid(row=10,column=4)
Label(root,text="Project Based Learning",font=("Aerial 20 bold"),fg="red").grid(row=11,column=4)

root.mainloop()
