import socket
from time import sleep

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Напишите exit для завершения работы с сервером')
msg = ''
while True:
    if msg != 'exit':
        print('Введите сообщение:')
        msg = input()
        sock.send(msg.encode())
        data = sock.recv(1024)
    else:
        break

sock.close()

print('Завершено')
