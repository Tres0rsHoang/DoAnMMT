from tkinter import *
from tkinter import messagebox

IP = '127.0.0.1'
Port = 1233

app = Tk()
app.geometry("500x300")
app.title("MainWindow")

def NewWindow():
    global IP
    IP = ''
    IP = Host.get()

def ProcessRunning():
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Close")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)

def AppRunning():
    newApp = Tk()
    newApp.geometry("450x300")
    newApp.title("listApp")
    kill = Button(
        newApp,
        text = "Kill",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 0, padx = 10, pady = 10)
    
    Xem = Button(
        newApp,
        text = "Xem",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 1, padx = 10, pady = 10)
    
    Xoa = Button(
        newApp,
        text =  "Xóa",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 2, padx = 10, pady = 10)

    Start = Button(
        newApp,
        text="Start",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 3, padx = 10, pady = 10)

    app = Tk()
    
def Close():
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Close")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)
def PrintScreen(): 
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("PrintScreen")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)
def Registry(): 
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Registry")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)
def Keystroke():
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Keystroke")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)
def Quit():
    click = messagebox.askyesno("Quit?", "Bạn chắc chắn muốn thoát")
    if click == 1:
        app.quit()
    else :
        return 0


Host = Entry(
    app, 
    width = 60
)
Host.insert(END, "Nhập IP của Server")
Host.grid(
    row=0,
    column=0, 
    columnspan = 3, 
    padx = 20, 
    pady = 20
)
Ketnoi = Button(
    app, 
    text="Kết nối", 
    padx = 15, 
    pady = 15, 
    command=NewWindow
).grid(row = 0, column = 3)

Process = Button(
    app, 
    text="Process Running", 
    padx = 0, 
    pady = 100, 
    command=ProcessRunning
).grid(row = 1, column = 0,padx = 0, pady = 0, rowspan = 3)

AppRun = Button(
    app, 
    text = "App Running", 
    padx = 80, 
    pady = 22, 
    command=AppRunning
).grid(row = 1, column = 1, columnspan = 2)

Close = Button(
    app, 
    text="Tắt máy", 
    padx = 15, 
    pady = 22, 
    command=Close
).grid(row = 2, column = 1)

PrintScreen = Button(
    app, 
    text="Chụp màn hình", 
    padx = 15, 
    pady = 22, 
    command=PrintScreen
).grid(row = 2, column = 2)

Registry = Button(
    app, 
    text="Sửa Registry", 
    padx = 85,
    pady = 22, 
    command=Registry
).grid(row = 3, column = 1, columnspan = 2)

Keystroke = Button(
    app, 
    text="Keystroke", 
    padx = 8, 
    pady = 60, 
    command=Keystroke
).grid(row = 1, column = 3, rowspan = 2)

Quit = Button(
    app, 
    text="Thoát",
    padx = 20,
    pady = 22, 
    command=Quit
).grid(row = 3, column = 3)

app.mainloop()
