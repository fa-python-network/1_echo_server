import socket
from re import match
import logging as log
from threading import Thread
from json import load, dump
from hashlib import md5
from strings import *

log.basicConfig(
                format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)


class Server:

    ADDRESS = ''
    PORT = 9797
    HOST_REGEX = r'[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}'
    RUNNING = True
    MAX_CONN = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.debug('Socket created')
        self.addr, self.port = self.ask_addr()
        self.bind()
        log.debug(f'Socket binded to port {self.port}')
        self.sock.listen(self.MAX_CONN)
        log.debug(f'Socket is listening {self.MAX_CONN} connections')
        self.mainloop()

    def mainloop(self):
        try:
            while 1:
                conn, addr = self.sock.accept()
                log.info(f'Connected {addr}')
                Thread(target=self.handle_client, args=(conn,)).start()
        finally:
            log.info('Server is closing')
            self.sock.close()

    def send(self, conn, msg):
        assert len(msg) <= 1020
        header = f'{len(msg):<4}'
        conn.send(f'{header}{msg}'.encode())
        log.debug(f'Sended msg: {msg}')

    def recv(self, conn):
        try:
            header = int(conn.recv(4).decode().strip())
        except ValueError:
            conn.close()
            return 'Connection closed'
        data = conn.recv(header).decode()
        log.debug(f'Received msg: {data}')
        return data

    def ask_addr(self):
        address_ = input(f'Address (empty for \'{self.ADDRESS}\'): ')
        port_ = input(f'Port (empty for {self.PORT}): ')
        return address_ if address_ and match(self.HOST_REGEX, address_) else self.ADDRESS, port_ if port_ and '1024' <= port_ <= '65535' else self.PORT

    def bind(self):
        try:
            self.sock.bind((self.addr, self.port))
        except OSError:
            self.sock.bind((self.addr, 0))
            self.port = self.sock.getsockname()[1]
            print(f'New PORT is {self.port}')

    def auth(self, conn):
        logged_in = False
        while not logged_in:
            self.send(conn, ask_username)
            uname = self.recv(conn)
            self.send(conn, ask_password)
            pwd = self.recv(conn)
            with open('users.json', 'r', encoding='utf-8') as f:
                users = load(f)
            if users.get(uname) == md5(pwd.encode()).hexdigest():
                self.send(conn, successful_login)
                logged_in = True
                log.debug(f'Successful login: {uname}')
                self.send(conn, greetings.format(uname))
            else:
                log.debug(f'Incorrect login: {uname}')
                self.send(conn, incorrect_password)
                self.send(conn, incorrect_password)


    def handle_client(self, conn):
        self.auth(conn)
        while 1:
            data = self.recv(conn)
            if data == 'Connection closed':
                break
            self.send(conn, data)


Server()
