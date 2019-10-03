import socket
import logging
import csv

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
log_handler = logging.FileHandler(filename = "info.log", encoding = "UTF-8")
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

stand_port = 9090
print("Введите номер порта: ")
inp_port = int(input())

if inp_port == 0:
	inp_port = stand_port
elif inp_port >=0 and inp_port <= 1024:
		print("Данный порт занят, введите новое значение: ")
		inp_port = int(input())

port = inp_port

sock = socket.socket()	
con_res = False
while con_res == False:
	try:
		sock.bind(('', port))
		con_res = True
	except OSError:
		port = port+1

if port != inp_port:
	print("Порт: ", inp_port, "занят; Прослушивается порт: ", port)
else:
	print("Прослушивается порт: ", port)

sock.listen(1)


while True:
	conn, addr = sock.accept()
	logger.info(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

	print(msg)

	conn.close()

