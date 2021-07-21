import socket

HOST = '127.0.0.1'
PORT = 8080

server_address = (HOST,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)
print("Connecting to server" + str(server_address))

try:
	while True:
		msg = input("Client: ")
		client.sendall(bytes(msg,"utf8"))
		if msg == "stop": break
		data = client.recv(1024)
		print("Server: ", data.decode("utf8"))
finally:
	client.close()