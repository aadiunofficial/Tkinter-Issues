import tkinter
from tkinter import Canvas
from popup import *
def openSender():    
    window = tkinter.Tk()
    window.title("STMTS")
    window.geometry("250x250")
    canvas = Canvas(window, width=250, height=250)
    canvas.pack()
    imagetest = tkinter.PhotoImage(file="Images/audac.png")
    canvas.create_image(250, 250, image=imagetest)
    label=tkinter.Label(window, text="Sender's End")
    label.place(x=90,y=10)
    v=tkinter.StringVar()
    senders_email=tkinter.StringVar()
    email_label=tkinter.Label(window, text="Send E-mail To:-")
    email_label.place(x=5,y=70)
    email_id=tkinter.Entry(window,width=20,textvariable=senders_email)
    email_id.place(x=120,y=70)
    email_label=tkinter.Label(window, text="Your Message :-")
    email_label.place(x=5,y=100)
    msg=tkinter.Entry(window,width=20,textvariable=v)
    msg.place(x=120,y=100)
#msg_label=tkinter.Label(window, text="Enter Your Message Here")
#msg_label.place(x=10,y=195)
#txt=tkinter.Entry(window,width=30,textvariable=v,selectborderwidth=10,show="*")
#txt.place(x=10,y=225)
    def clicked():
        v=msg.get()
        pop=" "
        t=0
        senders_email=email_id.get()
        if (len(senders_email)==0):
            pop="Invalid ID\n"
            t=1
        if (len(v)==0):
            pop+="Please Enter A Message"
            t=1
        if (t!=0):
            popupmsg(pop)
    image1=tkinter.PhotoImage(file="Images/mici1.png")
    button1=tkinter.Button(window,width=100,height=100,image=image1, command=clicked)
    button1.place(x=70,y=130)
    window.mainloop()

#openSender()
