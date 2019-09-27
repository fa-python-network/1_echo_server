import socket

sock = socket.socket()
num_port = input("Input port number to start a server")
try:
	num_port = int(num_port)
except:
	num_port = 4444
	print("incorrect format of port number")
sock.bind(('', num_port))
print("Server started working")
sock.listen(1)
print("Server started listening")
conn, addr = sock.accept()
client_name = conn.recv(1024)
print("Connected client ", addr, client_name.decode())

while True:
	print("Taking data from client")
	data = conn.recv(1024)
	if not data:
		print("Client didn't send data")
		break
	if data.decode() == "exit":
		print("Client want to disconnect")
		conn.close()
		print("Disconnection client")
		sock.listen(1)
		print("Server started listening")
		conn, addr = sock.accept()
		print("Connected client ", addr)
		continue
	print("Sending data to client")
	conn.send(data)

conn.close()
print("Disconnection client")
sock.close()
print("Shutdown server")
