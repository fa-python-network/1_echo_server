import socket


log_file = open('log.txt', 'w')
sock = socket.socket()

#print("Начало работы сервера")
print("Начало работы сервера", file = log_file)


client_host_port = 1024
while client_host_port != 65536:
	try:
		sock.bind(('', client_host_port))
		break
	except:
		client_host_port += 1

print("Подключение по порту:", client_host_port)
print("Подключение по порту: ", client_host_port, file = log_file)

sock.listen(1)
#print("Идёт прослушивание")
print("Идёт прослушивание", file = log_file)
log_file.close()


while True:
	try:
		ip_name_list_read = open('man.txt', 'r')
		conn, addr = sock.accept()
		print("Новое подключение:", addr)
		f = 0
		for line in ip_name_list_read:
			l = line.strip()
			if str(addr[0]) in l:
				name = l.split(':')[1]
				conn.send(("Good day, Dear{}\n".format(name)).encode())
				f = 1
				break
		while f == 0:
				ip_name_list_write = open("man.txt", 'a+')
				conn.send(("Enter your name:").encode())
				name1 = conn.recv(1024).decode()
				ip_name_list_write.write("{0} : {1}\n".format(addr[0], name1))
				ip_name_list_write.close()
				ip_name_list_read.close()
				break
		else:
			pass
	except socket.error:
		pass

	msg = ''
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		msg+=data
		conn.send(data.encode())
		print("Пользовательский ввод:", data)
		break
conn.close()
