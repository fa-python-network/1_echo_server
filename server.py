import socket
import json


def start_server():
	sock = socket.socket()
	num_port = input("Input port number to start a server: ")
	try:
		num_port = int(num_port)
		sock.bind(('', num_port))
	except ValueError:
		num_port = 4412
		sock.bind(('', num_port))
		f.write("Incorrect format of port number\n")
	except OSError:
		num_port += 11
		sock.bind(('', num_port))
		f.write("Port is already used, it was automaticly changed")

	print("Server is running on port " + str(num_port) + "\n")
	f.write("Server started working\n")
	sock.listen(1)
	f.write("Server started listening\n")
	return sock


f = open('log.txt', 'w')
sock = start_server()
conn, addr = sock.accept()
f.write("Connected client " + str(addr) + "\n")

with open("db.json", 'r') as file:
	db = json.load(file)

try:
	conn.send("OK".encode())
	conn.send(("Hello, "+db[addr[0]]).encode())
except:
	conn.send("FAIL".encode())
	client_name = conn.recv(1024)
	with open("db.json", 'w') as file:
		db[addr[0]] = client_name.decode()
		json.dump(db, file)

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
