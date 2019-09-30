import hashlib
import json
import random
import socket
from threading import Thread
import logging

logging.basicConfig(filename='server_logs.log', level=logging.INFO)

ENCODING = 'utf-8'
SALT = '//no_system_is_safe'.encode('utf-8')
COLORS = ['\33[31m', '\33[32m', '\33[33m', '\33[34m', '\33[35m', '\33[36m', '\33[91m', '\33[92m', '\33[93m', '\33[94m',
          '\33[95m', '\33[96m']
sock = socket.socket()
port = 9000
while True:
    try:
        sock.bind(('', port))
        break
    except OSError:
        port += 1
logging.info(f'Started on {socket.gethostbyname(socket.gethostname())}:{port}')
print(f'Started on {socket.gethostbyname(socket.gethostname())}:{port}')
sock.listen(10)

with open('users.json', 'r') as file:
    users = json.load(file)


def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)


connections_list = []


class CommonFunctions:
    @staticmethod
    def send_msg_all(message: str):
        [i.send_msg(message) for i in connections_list]

    @staticmethod
    def joined_chat(user: 'ClientThread'):
        [i.send_msg(f'\33[4m{user.username} joined this chat\33[0m') for i in connections_list if i != user]


class ClientThread(Thread):
    def __init__(self, connection: socket.socket, address: tuple):
        super().__init__(daemon=True)
        self.connected = True
        self.conn = connection
        self.addr = address
        self.username = 'UNSET'
        self.color = random.choice(COLORS)
        if addr[0] in users:
            self.send_msg('Enter password')
            if users[addr[0]]['password'] == hashlib.sha512(self.receive_msg().encode('utf-8') + SALT).hexdigest():
                self.username = users[addr[0]]['name']
                self.send_msg(f'Success login, {self.username}')
            else:
                self.send_msg('Password incorrect')
                self.send_msg(f'Closing connection {self.addr}')
                self.conn.close()
                logging.info(f'Connection closed {self.addr} - incorrect password')
        else:
            self.send_msg('Enter your name')
            name = self.receive_msg()
            self.username = name
            self.send_msg('Set new password')
            users.update({addr[0]: {'password': hashlib.sha512(self.receive_msg().encode('utf-8') + SALT).hexdigest(),
                                    'name': name}})
            save_users()

    def send_msg(self, message: str):
        if self.connected:
            self.conn.send(message.encode(ENCODING))

    def receive_msg(self):
        if not self.connected:
            return
        try:
            return self.conn.recv(1024).decode(ENCODING)
        except ConnectionResetError:
            connections_list.remove(thread)
            logging.info(f'Closing connection {self.addr}')
            self.connected = False

    def run(self):
        connections_list.append(self)
        self.send_msg(f'{self.username}, welcome to chat')
        while True and self.connected:
            message = self.receive_msg()
            if message == 'exit':
                self.send_msg(f'Closing connection {self.addr}')
                self.conn.close()
                logging.info(f'Connection closed {self.addr}')
                connections_list.remove(self)
                break
            CommonFunctions.send_msg_all(f'{self.color}{self.username}\33[0m: {message}')


while True:
    conn, addr = sock.accept()
    logging.info(f'Opening connection {addr} ')
    thread = ClientThread(conn, addr)

    thread.start()
