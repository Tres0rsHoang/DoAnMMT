from tkinter import *
from tkinter import messagebox
from Client import *
import tkinter as tk
import socket
from PIL import ImageTk,Image
from tkinter import filedialog
import tkinter

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
    newWin = Tk()
    #newWin.geometry("445x300")
    newWin.title("List Process Running")
    table = Frame(newWin, padx=20, pady = 20, borderwidth=5)
    table.grid(row=1,columnspan=5,padx=20)
    def PressXoaProcess():
        table.destroy()
    def PressXemProcess():
        nonlocal table
        size = 0
        list_id = [''] * 1000
        list_name = [''] * 1000
        list_thread = [''] * 1000
        client.sendall(bytes("Xem Process","utf8"))
        check = client.recv(1024).decode("utf8")

        size, list_id, list_name, list_thread = Recieve_Process_Running(client, HOST, PORT)

        table = Frame(newWin, padx=20, pady = 20, borderwidth=5)
        table.grid(row=1,columnspan=5,padx=20)
        
        from tkinter import ttk

        tree_scroll = Scrollbar(table)
        tree_scroll.pack(side=RIGHT,fill=Y)

        my_tree=ttk.Treeview(table, yscrollcommand=tree_scroll.set)
        my_tree.pack()

        tree_scroll.config(command=my_tree.yview)

        my_tree['columns'] = ("1","2") 
        my_tree.column("#0", anchor=CENTER, width =200,minwidth=25)
        my_tree.column("1", anchor=CENTER, width=60)
        my_tree.column("2", anchor=CENTER, width=100)

        my_tree.heading("#0", text="Name Process", anchor=W)
        my_tree.heading("1",text = "ID", anchor=CENTER)
        my_tree.heading("2", text = "Thread count", anchor=CENTER)

        for i in range(size):
            my_tree.insert(parent='', index='end',iid=0+i, text = list_name[i], values=(list_id[i],list_thread[i]))

        
    def PressKillProcess():
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
        def PressKill2Process():
            ID = enterID.get()
            client.sendall(bytes("Xoa Process","utf8"))
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
                command = PressKill2Process
            ).grid(row=0, column=4, padx=5, pady=5)
    def PressStartProcess():
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
        def PressStartProcess():
            Name = enterName.get()
            client.sendall(bytes("Bat Process","utf8"))
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
                command = PressStartProcess
            ).grid(row=0, column=4, padx=5, pady=5)

    kill = Button(
        newWin,
        text = "Kill",
        padx = 30, 
        pady = 20,
        command= PressKillProcess
        ).grid(row = 0, column = 0, padx = 10)
    Xem = Button(
        newWin,
        text = "Xem",
        padx = 30, 
        pady = 20,
        command = PressXemProcess
        ).grid(row = 0, column = 1, padx = 10)
    
    Xoa = Button(
        newWin,
        text =  "Xóa",
        padx = 30, 
        pady = 20,
        command = PressXoaProcess
        ).grid(row = 0, column = 2, padx = 10)

    Start = Button(
        newWin,
        text="Start",
        padx = 30, 
        pady = 20,
        command = PressStartProcess
    ).grid(row = 0, column = 3, padx = 10)

def Close():
    connect = messagebox.askyesno("Tắt máy", "Bạn có muốn tắt máy")
    if connect == 1:
        client.sendall(bytes("Shutdown","utf8"))
    else:
        return
        
def PrintScreen(): 
    newApp = Toplevel()
    newApp.title("PrintScreen")

    def Chup():
        client.sendall(bytes("Chup man hinh","utf8"))
        check = client.recv(1024).decode("utf8")

        myfile = open("anhcuatui.png", 'wb')
        data = client.recv(40960000)

        myfile.write(data)

        img = ImageTk.PhotoImage(Image.open("anhcuatui.png"))     
        canvas.create_image(0,0, anchor=NW, image=img)
        mainloop()

        myfile.close()

    def savefile():
        myScreenshot = open("anhcuatui.png",'rb')
        data = myScreenshot.read()
        fname = tkinter.filedialog.asksaveasfilename(title=u'Save file', filetypes=[("PNG", ".png")])
        myScreenshot.close()

        file = open(str(fname) + '.png','wb')
        file.write(data)
        file.close()

    canvas = Canvas(newApp, width = 500, height = 400)      
    canvas.grid(row=0,column=0)    

    but = Button(newApp,text="Chụp",width=5,height=10,borderwidth=5,command = Chup)
    but.grid(row=0,column=1)

    but1 = Button(newApp,text="Lưu",width=5,height=5,borderwidth=5,command=savefile)
    but1.grid(row=1,column=1)

def Registry(): 
    newApp = Tk()
    newApp.geometry("500x300")
    newApp.title("Registry")
    newApp = Label(newApp, text = "hi").grid(row = 0, column = 0)
def Keystroke():
    size = 0
    string = ''
    newApp = Tk()
    #newApp.geometry("500x300")
    newApp.title("Keystroke")  
    e = Entry(newApp, width = 55)
    e.grid(row = 1, column = 0,columnspan= 4)
    unhook_press = False
    def hook():
        nonlocal unhook_press
        unhook_press = False
        client.sendall(bytes("Hook Key","utf8"))
        check = client.recv(1024).decode("utf8")
    def unhook():
        nonlocal size, string, unhook_press
        if unhook_press == False:
            client.sendall(bytes("Unhook Key","utf8"))
            size , string = Recieve_Hook(client, HOST, PORT)
            unhook_press = True
    def xem():
        nonlocal size, string, unhook_press
        if unhook_press == False: 
            client.sendall(bytes("Unhook Key","utf8"))
            size , string = Recieve_Hook(client, HOST, PORT)
            unhook_press = True
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
        app.destroy()
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