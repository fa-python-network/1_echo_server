import socket
import logging as log
from re import match
from strings import *

log.basicConfig(filename='client.log', format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)


class Client:

    ADDRESS = 'localhost'
    PORT = 9797
    HOST_REGEX = r'[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}\.[1-2]?[0-9]{1, 2}'
    RUNNING = True
    MAX_CONN = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.debug('Socket started')
        self.addr, self.port = self.ask_addr()
        self.sock.connect((self.addr, self.port))
        self.auth()
        self.mainloop()


    def ask_addr(self):
        address_ = input(f'Address (empty for \'{self.ADDRESS}\'): ')
        port_ = input(f'Port (empty for {self.PORT}): ')
        return address_ if address_ and match(self.HOST_REGEX, address_) else self.ADDRESS, int(port_) if port_ and '1024' <= port_ <= '65535' else self.PORT

    
    def send(self, msg):
        assert len(msg) <= 1020
        header = f'{len(msg):<4}'
        self.sock.send(f'{header}{msg}'.encode())

    def recv(self):
        header = int(self.sock.recv(4).decode().strip())
        return self.sock.recv(header).decode()
    
    def auth(self):
        logged_in = False
        while not logged_in:
            uname = input(self.recv())
            self.send(uname)
            pwd = input(self.recv())
            self.send(pwd)
            result = self.recv()
            if result == successful_login:
                logged_in = True
            print(self.recv())

    def mainloop(self):
        msg = ''
        while msg != 'exit':
            msg = input('<= ')
            self.send(msg)
            print('=>', self.recv())



Client()
            
