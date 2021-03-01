import socket



class Server:
	PORT_NUMBER = 9090

	def __init__(self) -> None:
		sock = socket.socket()
		sock.bind(('', Server.PORT_NUMBER))
		sock.listen(0)
		#Наш сокет
		self.sock = sock
		#Текущее соединение
		print(f"Инициализировались, слушаем порт {Server.PORT_NUMBER}")
		#Ожидаем новое подключение
		while True:
			conn, addr = self.sock.accept()
			self.new_connection(conn, addr)
	
	def new_connection(self, conn, addr):
		"""
		Обработчик нового соединения
		"""
		print(f"Новое соединение от {addr}")
		msg = ''

		while True:
			#Получаем данные
			data = conn.recv(1024)
			
			#Если нет данных - больше ничего не ожидаем от клиента
			if not data:
				break

			msg += data.decode()
			conn.send(data)

			data_str = str(data, 'utf-8')
			print(f"Получили сообщение от клиента: '{data_str}'")

def main():
	server = Server()

if __name__ == "__main__":
	main()