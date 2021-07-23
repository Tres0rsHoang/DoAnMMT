from tkinter import *
from tkinter import messagebox
from Client import *
import tkinter as tk
import socket

HOST = '127.0.0.1'
PORT = 1233

app = Tk()
app.geometry("500x300")
app.title("MainWindow")

def NewWindow():
    global HOST
    global client
    HOST = Host.get()
    server_address = (HOST,PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(server_address)
        connected = messagebox.showinfo("Kết nối", "Bạn đã kết nối thành công!!!")
    except:
        connected = messagebox.showinfo("Kết nối", "IP sai")
def AppRunning():
    newWin = Tk()
    newWin.title("listApp")

    def PressXoa():
        table.destroy()
    def PressXem():
        global HOST
        global PORT
        global table
        size = 0
        list_id = [''] * 100
        list_name = [''] * 100
        list_thread = [''] * 100
        client.sendall(bytes("Xem App","utf8"))
        check = client.recv(1024).decode("utf8")
        size, list_id, list_name, list_thread = Recieve_App_Running(client, HOST, PORT)
        table = Frame(newWin, padx=20, pady = 20, borderwidth=5)
        table.grid(row=1,columnspan=5,padx=20)
        text = Label(
            table,
            text="Name Application"
            ).grid(row=0,column=0)
        text = Label(
            table,
            text="ID Application"
            ).grid(row=0,column=1)
        text = Label(
            table,
            text="Thread Count"
            ).grid(row=0,column=2)
        for i in range(size):
            text = Label(
                    table,
                    text = list_id[i]
                ).grid(row = i+1, column = 1)
            text = Label(
                    table,
                    text = list_name[i]
                ).grid(row = i+1, column = 0)
            text = Label(
                    table,
                    text = list_thread[i]
                ).grid(row=i+1,column = 2)
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
            client.sendall(bytes("Xoa App","utf8"))
            try:
                check = client.recv(1024).decode("utf8")
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
    def PressStart():
        newWin3 = Tk()
        newWin3.geometry("300x50")
        newWin3.title("Start")
        enterName = Entry(
                newWin3,
                width = 35
            )
        enterName.grid(
                row=0,
                column=0, 
                columnspan = 3,
                padx = 5,
                pady = 5 
            )
        enterName.insert(END,"Nhập Tên")
        def PressStart():
            Name = enterName.get()
            client.sendall(bytes("Bat App","utf8"))
            try:
                check = client.recv(1024).decode("utf8")
                client.sendall(bytes(Name,"utf8"))
                click = messagebox.showinfo("", "Chương trình đã bật")
            except:
                click = messagebox.showinfo("", "Không tìm thấy chương trình")

        bStart = Button(
                newWin3,
                text = "Start",
                padx = 20,
                command = PressStart
            ).grid(row=0, column=4, padx=5, pady=5)
    kill = Button(
        newWin,
        text = "Kill",
        padx = 30, 
        pady = 20,
        command= PressKill
    ).grid(row = 0, column = 0, padx = 10)
    Xem = Button(
        newWin,
        text = "Xem",
        padx = 30, 
        pady = 20,
        command = PressXem
    ).grid(row = 0, column = 1, padx = 10)
    
    Xoa = Button(
        newWin,
        text =  "Xóa",
        padx = 30, 
        pady = 20,
        command = PressXoa
    ).grid(row = 0, column = 2, padx = 10)

    Start = Button(
        newWin,
        text="Start",
        padx = 30, 
        pady = 20,
        command = PressStart
    ).grid(row = 0, column = 3, padx = 10)

def ProcessRunning():
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Close")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)


def Close():
    connect = messagebox.askyesno("tat may", "Ban muon tat may")
    if connect == 1:
        client.sendall(bytes("Shutdown","utf8"))
    else:
        return
        
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
    e = Entry(newApp, width = 55)
    e.grid(row = 1, column = 0,columnspan= 4)
    def hook():
        client.sendall(bytes("Hook Key","utf8"))
        check = client.recv(1024).decode("utf8")
    def unhook():
        client.sendall(bytes("Unhook Key","utf8"))
        
        size , string = Recieve_Hook(client, HOST, PORT)

    def xem():
        client.sendall(bytes("Xem key","utf8"))
        size , string = Recieve_Hook(client, HOST, PORT)
        e.delete(0,END)
        e.insert(0,string)
    def xoa():
        e.delete(0,END)

    Hook = Button(newApp, text = "Hook", padx = 20, pady = 20, command = hook).grid(row = 0,column = 0)
    unHook = Button(newApp, text = "Unhook", padx = 20, pady = 20, command = unhook).grid(row = 0,column = 1) 
    inphim = Button(newApp, text = "In phím", padx = 20, pady = 20,command = xem).grid(row = 0,column = 2)
    xoa = Button(newApp, text = "Xóa", padx = 20, pady = 20,command=xoa).grid(row = 0,column = 3)

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