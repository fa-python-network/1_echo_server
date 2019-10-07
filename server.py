import socket
import random


sock = socket.socket()
HOST = ''

log = open('log.txt', 'w')
log.write('Начало работы, подключаемся к клиенту...\n')


safe_port = random.randint(1025, 65535)

try:
	port_number = int(input('Введите номер порта от 1024 до 65535! Например, 8083: '))
	assert 1024 < port_number < 65535, 'Ну я тебя просил, а ты не слушал!'
#попробовал сделать рандомный порт, если ручной ввод не подходит
except:
	port_number = safe_port


while True:
	try:
		sock.bind((HOST, port_number))
		break
	except:
		port_number = safe_port



print(f'Номер порта = {port_number}')


log.write(f'Номер порта = {port_number}\n')
log.write('Сервер запущен, начинаем слушать порт!!\n')

while True:
	sock.listen(1)
	conn, addr = sock.accept()
	log.write(f'IP Адрес известен - {addr}\n')

	# print('Готов к обмену данными с клиентом')
	log.write('Готов к обмену данными с клиентом...\n')

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			msg += data.decode()
			conn.send(data.decode().upper().encode())

	print(msg, sep=' ') #хотел через sep сделать разделитель, но почему то не пошло!
	log.write('Сообщение отправлено и доставлено, завершаем работу!\n')
	log.close()
	conn.close()
