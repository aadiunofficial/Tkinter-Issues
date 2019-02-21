import tkinter
from tkinter import Canvas
def openReceiver():
    window = tkinter.Tk()
    window.title("STMTS")
    window.geometry("250x250")
    canvas = Canvas(window, width=250, height=250)
    canvas.pack()
    imagetest = tkinter.PhotoImage(file="Images/audac.png")
    canvas.create_image(250, 250, image=imagetest)
    label=tkinter.Label(window, text="Receiver's End")
    label.place(x=90,y=10)
    v=tkinter.StringVar()
    senders_email=tkinter.StringVar()
    email_label=tkinter.Label(window, text="Fetch Mail From :-")
    email_label.place(x=5,y=70)

    email_id=tkinter.Entry(window,width=20,textvariable=senders_email)
    email_id.place(x=120,y=70)

    image1=tkinter.PhotoImage(file="Images/speaker2.png")
    button1=tkinter.Button(window,width=100,height=100,image=image1)
    button1.place(x=70,y=130)
    window.mainloop()
openReceiver()
