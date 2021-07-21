import socket

HOST = '127.0.0.1'
PORT = 1233

server_address = (HOST,PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)
print("Connecting to server" + str(server_address))

def Recieve_App_Running(HOST, PORT):
	list_id = ['']*100
	list_name = ['']*100
	list_thread = ['']*100
	size = 0

	size = client.recv(1024).decode("utf8")
	size = int(size)
	for i in range(size):
		data = client.recv(1024).decode("utf8")
		list_id[i] = data
		client.sendall(bytes(data,"utf8"))

	for i in range(size):
		data = client.recv(1024).decode("utf8")
		list_name[i] = data
		client.sendall(bytes(data,"utf8"))

	for i in range(size):
		data = client.recv(1024).decode("utf8")
		list_thread[i] = data
		client.sendall(bytes(data,"utf8"))
	for i in range(size):
		print(list_id[i], list_name[i], list_thread[i])
	return size, list_id, list_name, list_thread

Recieve_App_Running(HOST, PORT)