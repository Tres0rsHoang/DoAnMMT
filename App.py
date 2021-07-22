from tkinter import *
from tkinter import messagebox
from Client import *
import tkinter as tk
import socket

IP = '127.0.0.1'
Port = 1233
server_address = (IP,Port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(server_address)
    print("Connecting to server" + str(server_address))
except:
    print("Can\'t connect to server...")

app = Tk()
app.geometry("500x300")
app.title("MainWindow")

def NewWindow():
    global IP
    IP = ''
    IP = Host.get()

def AppRunning():
    newWin = Tk()
    newWin.geometry("450x300")
    newWin.title("listApp")

    def PressXem():
        global IP
        global Port
        size = 0
        list_id = [''] * 100
        list_name = [''] * 100
        list_thread = [''] * 100
        client.sendall(bytes("Xem App","utf8"))
        size, list_id, list_name, list_thread = Recieve_App_Running(client, IP, Port)
        text = Label(
            newWin,
            text="Name Application"
            ).grid(row=1,column=0)
        text = Label(
            newWin,
            text="ID Application"
            ).grid(row=1,column=1)
        text = Label(
            newWin,
            text="Thread Count"
            ).grid(row=1,column=2)
        for i in range(size):
            text = Label(
                    newWin,
                    text = list_id[i]
                ).grid(row = 2+i, column = 1)
            text = Label(
                    newWin,
                    text = list_name[i]
                ).grid(row = 2+i, column = 0)
            text = Label(
                    newWin,
                    text = list_thread[i]
                ).grid(row=2+i,column = 2)

    def PressKill():
        newWin2 = Tk()
        newWin2.geometry("300x50")
        newWin2.title("Kill")
        enterID = Entry(
                newWin2,
                width = 35
            )
        enterID.grid(
                row=0,
                column=0, 
                columnspan = 3,
                padx = 5,
                pady = 5 
            )
        enterID.insert(END,"Nhập ID")
        def PressKill2():
            ID = enterID.get()
            print(ID)
            client.sendall(bytes("Xoa App","utf8"))
            try:
                check = client.recv(1024).decode("utf8")
                print(check)
                client.sendall(bytes(ID,"utf8"))
                click = messagebox.showinfo("", "Đã diệt chương trình")
            except:
                click = messagebox.showinfo("", "Không tìm thấy chương trình")

        bKill = Button(
                newWin2,
                text = "Kill",
                padx = 20,
                command = PressKill2
            ).grid(row=0, column=4, padx=5, pady=5)
        
        
    kill = Button(
        newWin,
        text = "Kill",
        padx = 30, 
        pady = 20,
        command= PressKill
    ).grid(row = 0, column = 0, padx = 10, pady = 10)
    
    Xem = Button(
        newWin,
        text = "Xem",
        padx = 30, 
        pady = 20,
        command = PressXem
    ).grid(row = 0, column = 1, padx = 10, pady = 10)
    
    Xoa = Button(
        newWin,
        text =  "Xóa",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 2, padx = 10, pady = 10)

    Start = Button(
        newWin,
        text="Start",
        padx = 30, 
        pady = 20
    ).grid(row = 0, column = 3, padx = 10, pady = 10)


def ProcessRunning():
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Close")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)

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
