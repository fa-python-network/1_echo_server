import socket
import json

f = open ('log.txt', 'w')

# Перебираем порты
sock = socket.socket()
port = 9090
while True:
	try:
		if (port == 65536):
			print('Все порты заняты')
			break
		sock.bind(('', port))
		break
	except:
		port += 1

print(f'Port number: {port}')
print("Server starts", file = f)
sock.listen(0)
print("Now listen", file = f)

while True:
	conn, addr = sock.accept()
	# Открываю json
	with open('base.json', 'r+') as d:
		data = json.loads(d.read())
		# Перебираю знакомые айпи
		for i in data['clients']:
			if i['ip'] == addr[0]:
				hello = f"Hello {i['name']}"
				conn.send(hello.encode())
				# Проверка правильности пароля
				while True:
					conn.send(b'Input your password:')
					passwd = conn.recv(1024).decode()
					if i['password'] == passwd:
						conn.send(b'Correct password!')
						break
					else:
						conn.send(b'Wrong password! Try another')
				break
		else:
			# Добавляю нового пользователя
			conn.send(b'Input your name:')
			name = conn.recv(1024).decode()
			conn.send(b'Input your password:')
			passwd = conn.recv(1024).decode()
			newClient = {"ip": addr[0], "name": name, "password": passwd}
			data['clients'].append(newClient)
			d.seek(0)
			d.write(json.dumps(data))


	msg = ''
	while True:
		data = conn.recv(1024)
		print("new data from client", file = f)
		if not data:
			break
		msg = msg + data.decode() + ' '
		conn.send(data)

	print("data to client", file = f)
	print(f'Сообщение от пользователя: "{msg}"')
	conn.close()
	print('stop client', file = f)
	# Остановка сервера
	i = input('Если вы хотите остановить сервер введите: "stop"\n ')
	if i == 'stop':
		sock.close()
		print('stop client', file = f)
		f.close()
		break
		
