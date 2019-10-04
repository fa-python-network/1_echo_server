import json
import random
import socket
from threading import Thread
import logging
from common import COLORS, SALT, EMOJIS, EMOJIS_PATTERN, SocketMethods, Security

logging.basicConfig(filename='server_logs.log', level=logging.INFO)


def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)


users = {}
connections_list = []


class CommonFunctions:
    @classmethod
    def send_msg_all(cls, message: str):
        [i.send_msg(message) for i in connections_list]

    @staticmethod
    def service_msg(user: 'ClientThread', message: str):
        [i.send_msg(f'\33[4m{user.username} {message}\33[0m') for i in connections_list if i != user]

    @staticmethod
    def _emoji_replace(match) -> str:
        mg = match.group(1)
        return EMOJIS.get(mg, f':{mg}:')

    @classmethod
    def emoji_replace(cls, s: str) -> str:
        return EMOJIS_PATTERN.sub(cls._emoji_replace, s)


class ClientThread(Thread):
    def __init__(self, connection: socket.socket, address: tuple):
        super().__init__(daemon=True)
        self.connected = True
        self.conn = connection
        self.addr = address
        self.username = 'UNSET'
        self.color = random.choice(COLORS)
        token = self.receive_msg()
        if addr[0] in users:
            if users[addr[0]]['token'] == token:
                self.success_login()
            else:
                self.send_msg('Enter password')
                if users[addr[0]]['password'] == Security.get_password_hash(self.receive_msg()):
                    self.success_login()
                else:
                    self.send_msg('Password incorrect')
                    self.send_msg(f'Closing connection {self.addr}')
                    self.send_msg('//close')
                    self.conn.close()
                    logging.info(f'Connection closed {self.addr} - incorrect password')
        else:
            self.send_msg('Enter your name')
            name = self.receive_msg()
            self.username = name
            self.send_msg('Set new password')
            users.update({addr[0]: {'password': Security.get_password_hash(self.receive_msg()),
                                    'name': name}})
            save_users()

    def success_login(self):
        self.username = users[addr[0]]['name']
        self.send_msg(f'Success login')
        new_token = Security.get_new_token()
        self.send_msg('//token')
        self.send_msg(new_token)
        users[addr[0]]['token'] = new_token
        save_users()

    def send_msg(self, message: str):
        if self.connected:
            SocketMethods.send_text(self.conn, message)

    def receive_msg(self):
        if not self.connected:
            return
        try:
            return SocketMethods.receive_text(self.conn)
        except ConnectionResetError:
            connections_list.remove(thread)
            logging.info(f'Closing connection {self.addr}')
            self.connected = False

    def run(self):
        connections_list.append(self)
        self.send_msg(f'{self.username}, welcome to chat')
        CommonFunctions.service_msg(self, 'joined the chat')
        while True and self.connected:
            message = self.receive_msg()
            if message == 'exit':
                self.send_msg(f'Closing connection {self.addr}')
                self.send_msg('//close')
                self.conn.close()
                logging.info(f'Connection closed {self.addr}')
                connections_list.remove(self)
                self.connected = False
                break
            CommonFunctions.send_msg_all(f'{self.color}{self.username}\33[0m: {CommonFunctions.emoji_replace(message)}')


if __name__ == '__main__':
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
    while True:
        conn, addr = sock.accept()
        logging.info(f'Opening connection {addr} ')
        thread = ClientThread(conn, addr)

        thread.start()
