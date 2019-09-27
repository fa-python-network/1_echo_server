import socket
import json
sock = socket.socket()
sock.bind(('10.38.165.12', 9090))
sock.listen(4)
command = ("exit")
while True
	conn, addr = sock.accept()
	print(addr)
	data = 'new'
	while data:
		data = conn.recv(1024)
		data = data.decode()
		if data not in command:
			print(data)
		else:
			with open("log_serv.json", "a") as file:
				json.dump(data, file)
			





