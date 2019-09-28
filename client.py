import socket


def settings():
	"""
	Настройка подключения к серверу
	"""
	host_prompt = input('Type the HOST if needed: ')
	port_prompt = input('Type the PORT if needed: ')

	global HOST
	global PORT
	HOST = '127.0.0.1' if not host_prompt else host_prompt
	PORT = 9014 if not port_prompt else int(port_prompt)


if __name__ == '__main__':
    settings()

    with socket.socket() as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hi, dingus')

        while True:
            data = s.recv(1024)
            s.sendall(bytes(input(), 'utf-8'))

    print(f'Received {data}')
