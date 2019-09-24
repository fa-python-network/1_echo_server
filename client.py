import socket
from time import sleep

sock = socket.socket()

print("Write port number")
portnum = int(input())
print("Write host name")
hostname = str(input())

sock.setblocking(1)
sock.connect((hostname, portnum))

print("Write <exit> to quit")

while True:
	msg = input()
	if msg == "exit":
		sock.send("Client exit".encode())
		break
	sock.send(msg.encode())

	data = sock.recv(1024)

sock.close()

print(data.decode())
