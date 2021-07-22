import socket

def Recieve_App_Running(client, HOST, PORT):
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
	return size, list_id, list_name, list_thread

#Recieve_App_Running(HOST, PORT)
def Recieve_Hook(client, HOST, PORT):
	size =0
	size = client.recv(1024).decode("utf8")
	size = int(size)
	
	data = client.recv(1024).decode("utf8")
	list_string= data
	client.sendall(bytes(data,"utf8"))
	print(list_string)	

	return size, list_string
