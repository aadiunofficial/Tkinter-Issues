import tkinter
import sender
import receive 
window = tkinter.Tk()
window.title("STMTS")
image1=tkinter.PhotoImage(file="Images/audac.png")
Label=tkinter.Label(window, text="Welcome To STMTS")
Label.pack()
button1=tkinter.Button(window,width=80,height=80,image=image1,command=sender.openSender)
button2=tkinter.Button(window,width=80,height=80,image=image1,command=receive.openReceiver)


button1.pack(side="left")
button2.pack(side="right")
tkinter.Label(window, text="All Equals!").pack()
tkinter.Label(window, text="All Equals!").pack()
window.mainloop()
