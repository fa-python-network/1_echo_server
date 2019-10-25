import socket
import json

def write_into_json(dct):
	with open('users.json', 'w') as f:
		json.dump(dct, f)
users = {}

port = 9089
file = open("logfile.txt", "a")
sock = socket.socket()

with open('users.json','r') as f:
	users = json.load(f)

try:
	sock.bind(('', port))
except OSError: 
	sock.bind(('',0))
	port = sock.getsockname()[1]
	print(f"use port {port}")
	file.write(f'Сервер использует порт{port}\n')
sock.listen(1)
file.write(f'Сервер слушает клиента{port}\n')

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
 	msg_to_client = f'Hi,{users[addr[0]]}!'
 	conn.send(msg_to_client.encode())
 	write_into_json(users)

	msg = ''

	while True:
		file.write(f'Сервер получает данные{addr}\n')
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
		conn.send(data)
		print(msg)
	file.write(f'Сервер отвечает\n')
file.close()
conn.close()
