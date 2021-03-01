import socket

PORT_NUMBER = 9090

def main():
	print(f"Запустили сервер, слушаем порт {PORT_NUMBER}")
	sock = socket.socket()
	sock.bind(('', PORT_NUMBER))
	sock.listen(0)
	conn, addr = sock.accept()
	print(f"Новое соединение от {addr}")

	msg = ''

	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

		data_str = str(data, 'utf-8')
		print(f"Получили сообщение от клиента: '{data_str}'")



	conn.close()

if __name__ == "__main__":
	main()