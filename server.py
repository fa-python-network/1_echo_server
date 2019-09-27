import json
import socket
from threading import Thread
import logging

logging.basicConfig(filename='server_logs.log', level=logging.INFO)

ENCODING = 'utf-8'
sock = socket.socket()
i = 9000
while True:
    try:
        sock.bind(('localhost', i))
        print('Port: ', i)
        break
    except OSError:
        i += 1
logging.info(f'Started on port {i}')
sock.listen(10)

users = {}
with open('users.json', 'r') as file:
    users = json.load(file)


class ClientThread(Thread):
    def __init__(self, connection, addres):
        super().__init__()
        self.conn = connection
        self.addr = addres
        if addr[0] in users:
            self.conn.send(f'Enter password'.encode(ENCODING))
            if users[addr[0]] == self.conn.recv(1024).decode(ENCODING):
                self.conn.send(f'Enter password'.encode(ENCODING))
            else:
                self.conn.send(f'Password incorrect'.encode(ENCODING))
                self.conn.send(f'Closing connection {self.addr}'.encode(ENCODING))
                self.conn.close()
                logging.info(f'Connection closed {self.addr} - incorrect password')
        else:
            self.conn.send(f'Set new password'.encode(ENCODING))
            users.update({addr[0]: self.conn.recv(1024).decode(ENCODING)})

    def run(self):
        while True:
            message = self.conn.recv(1024).decode(ENCODING)
            print(message)
            if message == 'exit':
                self.conn.send(f'Closing connection {self.addr}'.encode(ENCODING))
                self.conn.close()
                logging.info(f'Connection closed {self.addr}')
                break
            self.conn.send(message.encode(ENCODING))


while True:
    conn, addr = sock.accept()
    thread = ClientThread(conn, addr)
    thread.start()
