import socket

HOST = '127.0.0.1'  
PORT = 1233
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
client, addr = server.accept()
print('Connected by', addr)

def App_running(HOST, PORT):
    import subprocess
    cmd = 'powershell "Get-Process |where {$_.mainWindowTItle} |format-table id,name'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            print(line.decode().rstrip().lstrip())
    count = 0
    size = 0
    list_name = ['' for i in range(100)]
    list_id = ['' for i in range(100)]
    for line in proc.stdout:
        if line.rstrip():
            if count < 2:
                count += 1
                continue
            str_line = str(line.decode().rstrip().lstrip())
            list_id_name = str_line.split(" ")
            list_name[size] = list_id_name[1]
            list_id[size] = list_id_name[0]
            size += 1
    client.sendall(bytes(str(size),"utf8"))
    for i in range(size):
        client.send(bytes(list_id[i],"utf8"))
        check = client.recv(1024)
    for i in range(size):
        client.sendall(bytes(list_name[i], "utf8"))
        check = client.recv(1024)

try:
    App_running(HOST,PORT)
finally:
    server.close()