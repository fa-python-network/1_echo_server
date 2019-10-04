import socket
import time
import json
from os import listdir
import hashlib
import re


def settings() -> None:
	host_prompt = input('Type the HOST if needed: ')
	port_prompt = input('Type the PORT if needed: ')

	global HOST
	global PORT
	HOST = '127.0.0.1' if not host_prompt else host_prompt
	PORT = 0 if not port_prompt else int(port_prompt)


def write_to_file(msg: str, filename='log') -> None:
	with open(filename, 'a') as f:
		f.write(f'-----------------------\ntime: {time.time()}\nmsg: {msg}\n')


def register_new_client(ip_address: str, user_name: str, password: str) -> None:
	user_db[ip_address] = {'user_name': user_name, 'password': password}

	with open('user_db', 'w') as f:
		json.dump(user_db, f)
	
	write_to_file('----Successfully added a new client----')


if __name__ == '__main__':
	settings()

	if 'user_db' not in listdir():
		with open('user_db', 'w') as f:
			f.write('{}')
		print('----No user database existed; created a new one----')
	
	with open('user_db', 'r') as f:
		user_db = json.load(f)
		print('----Successfully loaded the user database----')

	with socket.socket() as s:
		s.bind((HOST, PORT))
		print(f'The port is {s.getsockname()[1]}')
		s.listen()

		while True:
			conn, addr = s.accept()

			write_to_file('----Accepted a new request----')

			with conn:
				write_to_file(f'----Connected by {addr}----')

				if addr[0] not in user_db:
					conn.sendall(b'You\'re not in the records. Send us your new user name and password as follows:\nUSER_NAME;PASSWORD')
				else:
					conn.sendall(b'Enter the password, please')
					data = conn.recv(1024)
					if data.decode() == user_db[addr[0]]['password']:
						conn.sendall(f'Welcome back, {user_db[addr[0]]["user_name"]}'.encode())
				
				while True:
					
					data = conn.recv(1024)

					if addr[0] not in user_db:
						if re.match(r'(\w+);(\w+)', data.decode()):
							reply = re.search(r'(\w+);(\w+)', data.decode())
							user_name, password = reply.group(1), reply.group(2)
							register_new_client(addr[0], user_name, password)
						else:
							continue

					write_to_file(data.decode())

					if not data or data == b'exit':
						write_to_file('----Stopped serving a user----')
						break
