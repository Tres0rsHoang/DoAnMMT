
def Server_Running():

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

    while True:
        try:
            def Command_catch(i):
                if i == "Xem App": App_running(HOST,PORT)
                elif i == "Xoa App": 
                    ID_App = client.recv(1024).decode("utf8") 
                    App_running_kill(ID_App)
            Command = client.recv(1024).decode("utf8")
            client.sendall(bytes("OK","utf8"))
            print(Command)
            Command_catch(Command)
        except:
            print("Disconnected")
            break

from tkinter import *
from tkinter import messagebox

mainWin = Tk()
Start = Button(
        mainWin,
        text = "Khởi động server",
        width = 25,
        height = 25,
        command = Server_Running
    ).pack()
mainWin.mainloop()
