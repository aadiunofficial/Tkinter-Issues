import tkinter
def popupmsg(msg):
    popup = tkinter.Tk()
    popup.wm_title("!")
    label = tkinter.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="  Ok  ", command = popup.destroy,bg="lightgreen")
    B1.pack()
    popup.mainloop()

