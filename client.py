import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

print('Для выхода введите команду "exit".')

msg = ''

while msg != 'exit':
    print('Введите сообщение:')
    msg = input()
    sock.send(msg.encode())
    data = sock.recv(1024)

sock.close()
