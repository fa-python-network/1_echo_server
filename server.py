import socket
import time


def settings():
	"""
	Настройка сервера
	"""
	host_prompt = input('Type the HOST if needed: ')
	port_prompt = input('Type the PORT if needed: ')

	global HOST
	global PORT
	HOST = '127.0.0.1' if not host_prompt else host_prompt
	PORT = 9014 if not port_prompt else int(port_prompt)


def write_to_file(msg: str, filename='log.txt'):
	"""
	Записівает сообщения в файл
	"""
	with open(filename, 'a') as f:
		f.write(f'-----------------------\ntime: {time.time()}\nmsg: {msg}\n')


if __name__ == '__main__':
	settings()

	with socket.socket() as s:
		s.bind((HOST, PORT))
		s.listen()

		while True:
			conn, addr = s.accept()

			write_to_file('Accepted a new request')

			with conn:
				write_to_file(f'Connected by {addr}')

				while True:
					data = conn.recv(1024)
					write_to_file(data.decode())

					if not data or data == b'exit':
						write_to_file('Stopped serving a user')
						break

					conn.sendall(data)
