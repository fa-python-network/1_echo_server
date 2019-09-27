import socket

sock = socket.socket()
f = open('log.txt', 'w')
num_port = input("Input port number to start a server: ")
try:
	num_port = int(num_port)
except:
	num_port = 4445
	f.write("Incorrect format of port number\n")
sock.bind(('', num_port))
f.write("Server started working\n")
sock.listen(1)
f.write("Server started listening\n")
conn, addr = sock.accept()
client_name = conn.recv(1024)
f.write("Connected client " + str(addr) + str(client_name.decode()) + "\n")

while True:
	f.write("Taking data from client\n")
	data = conn.recv(1024)
	if not data:
		f.write("Client didn't send data\n")
		break
	if data.decode() == "exit":
		f.write("Client want to disconnect\n")
		conn.close()
		f.write("Disconnection client\n")
		sock.listen(1)
		f.write("Server started listening\n")
		tmp = input("If you want to shutdown server - input 'stop', else - input any text: ")
		if tmp == "stop":
			break
		conn, addr = sock.accept()
		f.write("Connected client " + str(addr))
		continue
	f.write("Sending data to client\n")
	conn.send(data)

sock.close()
f.write("Shutdown server\n")
f.close()
