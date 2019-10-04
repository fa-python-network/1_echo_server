import socket
import json


def write_into_json(dct):
	with open('users.json', 'w') as f:
		json.dump(dct, f)


users = {}
port = 9090
file = open("log.txt", "a")
sock = socket.socket()

#open file to take dict from it
with open('users.json','r') as f:
	users = json.load(f)

try:
	sock.bind(('', port))
except OSError: 
	sock.bind(('',0))
	port = sock.getsockname()[1]
	print(f"use port {port}")
file.write(f'server uses port {port}\n')

sock.listen()
file.write(f'server starts listen client\n')


while True:
	conn, addr = sock.accept()
	print(addr[0])
	try:
		c = users[addr[0]]
	except KeyError:
		conn.send(b"What is your name?")
		users[addr[0]] = (conn.recv(1024)).decode()
		print(users[addr[0]])
	msg_to_client = 'Hi,'+{users[addr[0]]}+'!'
	conn.send(msg_to_client.encode())
	write_into_json(users)	

	msg = ""

	while True:
		file.write(f'server receives datd from client {addr}\n')
		data = conn.recv(1024)
		if not data:
			break
		print(data.decode())
		conn.send(data)
		file.write(f'server responds to a client\n')


file.close()
conn.close()
