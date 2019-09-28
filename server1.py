import logging

server1_log = logging.FileHandler('server1.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(server1_log, console_out),
format='[%(asctime)s | %(levelname)s]: %(message)s',
datefmt = '%m.%d.%Y %H:%M:%S',
level = logging.INFO)



import socket

sock = socket.socket()
port = 9080
sock.bind(('', port))
logging.info("Запустили сервер")

sock.listen(1)
logging.info("Начинаем прослушивать порт")
while True:
	conn, addr = sock.accept()
	logging.info(f"Подключение клиента с адрессом {addr}")

	logging.info("Прием данных от клиента")
	msg=''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg+=data.decode()
	logging.info(msg)

	conn.close()

logging.info("Отключение клиента")
logging.info("Остановка сервера")
