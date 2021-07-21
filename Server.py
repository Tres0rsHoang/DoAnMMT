import socket

HOST = '127.0.0.1'  
PORT = 8080      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

try:
    while True:
        client, addr = server.accept()
        try:
            print('Connected by', addr)
            while True:
                msg = client.recv(1024)
                str_msg = msg.decode("utf8")
                if str_msg == "stop": break
                print("Client: ", str_msg)
                data = input("Server: ")
                client.sendall(bytes(data,"utf8"))
        finally:
            client.close()
finally:
    server.close()