#logging
import logging
log_file = logging.FileHandler('myserver.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(log_file, console_out), format = '[%(asctime)s | %(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S' , level = logging.INFO)

logging.info('Start')


import socket

sock = socket.socket()

port = 8080
sock.bind(('', port))
logging.info(f'Сервер подключился к порту {port}')

count_of_clients = 1
sock.listen(count_of_clients)
logging.info(f'Сервер готов к прослушиванию')

while True:
	conn, addr = sock.accept()
	logging.info(f'Сервер подключился к клиенту {addr}')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data)
		logging.info('Отправка сообщения клиенту')
	conn.close()
	logging.info('Соединение завершено')





