import socket
import json

f = open ('log.txt', 'w')

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
	with open('base.json', 'r') as d:
		data = json.loads(d.read())
		for i in data['clients']:
			if i['ip'] == addr[0]:
				print("Салам алейкум")

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
	i = input('Если вы хотите остановить сервер введите: "stop"\n ')
	if i == 'stop':
		sock.close()
		print('stop client', file = f)
		f.close()
		break
		
