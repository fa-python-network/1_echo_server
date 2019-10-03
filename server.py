import socket

txt = open('log.txt', 'w')
sock = socket.socket()

#print("Начало работы сервера")
print("Начало работы сервера", file = txt)

cl_host_port = 1024
while cl_host_port != 65536:
	try:
		sock.bind(('', cl_host_port))
		break
	except:
		cl_host_port += 1

print("Подключение по порту:", cl_host_port)
print("Подключение по порту: ", cl_host_port, file = txt)

sock.listen(0)
#print("Идёт прослушивание")
print("Идёт прослушивание", file = txt)

while True:
	try:
		conn, addr = sock.accept()
		print("Новое подключение:", addr)
	except sock.error:
		pass
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
		conn.send(data)
	print("Пользовательский ввод:", msg)
conn.close()
