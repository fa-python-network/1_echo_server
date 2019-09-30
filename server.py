import socket
import sys

def close_server():
	with open ('log.txt', 'a') as file:
		print('Остановка сервера', file=file)
	global sock
	sock.close()
	sys.exit()

try: 
	sock = socket.socket()
except KeyboardInterrupt:
	close_server()


sock.bind(('', 9090))
with open ('log.txt', 'a') as file:
		print('Запуск сервера', file=file)
try:
	sock.listen(1)
	with open ('log.txt', 'a') as file:
		print('Начало прослушивания порта', file=file)
except KeyboardInterrupt:
	close_server()

while True:

	try:
		conn, addr = sock.accept()
		with open ('log.txt', 'a') as file:
			print('Подключение клиента', file=file)
	except KeyboardInterrupt:
		close_server()			

	while True:
		try:
			data = conn.recv(1024).decode()
			with open ('log.txt', 'a') as file:
				print('Приём данных от клиента', file=file)
		except KeyboardInterrupt:
			close_server()
		if not data:
			conn.close()
			break
		try:
			conn.send(data.upper().encode())
			with open ('log.txt', 'a') as file:
				print('Отправка данных клиенту', file=file)
		except KeyboardInterrupt:
			close_server()

	with open ('log.txt', 'a') as file:
		print('Отключение клиента', file=file)



