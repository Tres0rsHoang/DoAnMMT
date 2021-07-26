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
	
def Recieve_Hook(client):
	data = client.recv(1024).decode("utf8")
	list_string = data
	client.sendall(bytes(data,"utf8"))	
	return list_string

	return size, list_string
def Recieve_Process_Running(client, HOST, PORT):
    list_id = ['']*1000
    list_name = ['']*1000
    list_thread = ['']*1000
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
def Recieve_Reg_Value(client):
	data = client.recv(1024).decode("utf8")
	client.sendall(bytes("Da nhan", "utf8"))
	return data
