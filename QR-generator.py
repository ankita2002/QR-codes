from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

heading = Tk()
heading.title("QR-Code Generator")
myQr = None
photo = None


def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        QRimage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data = QRimage)
    else:
        messagebox.showinfo("Error!!!")
    try:
        showcode()
    except:
        pass

def showcode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="QR-code :" +subject.get())

def save():
    dir = path1 = os.getcwd() 

    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) !=0:
            QRimage = myQr.png(os.path.join(dir,name.get()+".png"), scale=6)
        else:
            messagebox.showinfo("Error! File name cannot empty...")
    except:
        messagebox.showinfo("ERROR !!! Generate the code first")

lab1 = Label(heading,text="Enter Subject",font=("Helvetica",12))
lab1.grid(row=0, column=0, sticky=N+S+E+W)
    
lab2 = Label(heading,text="Enter File Name",font=("Helvetica",12))
lab2.grid(row=1, column=0, sticky=N+S+E+W)

subject = StringVar()
subjectEntry = Entry(heading, textvariable=subject,font=("Helvetica",12))
subjectEntry.grid(row=0,column=1, sticky=N+S+E+W)

name = StringVar
nameEntry = Entry(heading, textvariable=name,font=("Helvetica",12))
nameEntry.grid(row=1,column=1, sticky=N+S+E+W)

Create = Button(heading,text="Create QR-Code",font=("Helvetica",12), width=15,command=generate)
Create.grid(row=0,column=3, sticky=N+S+E+W)

notificationLabel = Label(heading)
notificationLabel.grid(row=2,column=1,sticky=N+S+E+W)

subLabel = Label(heading,text="")
subLabel.grid(row=3,column=1, sticky=N+S+E+W)

show = Button(heading,text="Save as PNG",font=("Helvetica",12),width=15,command=save)
show.grid(row=1,column=3, sticky=N+S+E+W)

trows = 3
tcols = 3
for row in range(trows+1):
    heading.grid_rowconfigure(row, weight=1)
for col in range(tcols+1):
    heading.grid_columnconfigure(col, weight=1)

heading.mainloop()