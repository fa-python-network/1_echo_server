import socket

port = 9089
file = open("logfile.txt", "a")
sock = socket.socket()
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
	try:
		conn, addr = sock.accept()
	except sock.error:
		pass
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
