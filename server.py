import socket
from datetime import datetime

def log(data):
	with open("logs.log", "a") as file1:
		print(str(datetime.now())+ " | " + data, file=file1)



host = input('Введите хост: ')
while True:
	port = input('Введите порта: ')
	try:
		port = int(port)
		if 100 <= port <= 65535:
			break
		print("Неправильный диапазон")
	except ValueError:
		print("Неправильный порт")
log(f"Запуск сервера")
sock = socket.socket() 
sock.bind((host, port)) 
sock.listen(1)
log(f"Начало прослушивания порта")

while True:
	
	conn, addr = sock.accept()
	log(f"Клиент {addr[0]}:{addr[0]} подключился")

	msg = ''

	while True: 
		data = conn.recv(1024) 
		log(f"Получает новые данные от пользователя {addr[0]}:{addr[0]}")
		if not data: 
			msg += data.decode("utf-8") 
			conn.send(data) 
			log(f"Отправка '{data}' пользователю {addr[0]}:{addr[0]}")
	log(f"Пользователь {addr[0]}:{addr[0]} отключился")
	print(msg) 

conn.close()
log("Сервер выключился")