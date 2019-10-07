import socket
import re

sock = socket.socket()
sock.setblocking(1)

host = input('Введите имя хоста:')

if host != 'localhost':
    cond = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)
else:
    host = '127.0.0.1'
    
while (cond == False):
    host = input('Имя хоста введено неверно. Введите имя хоста:')
    cond = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host)

port = int(input('Введите номер порта:'))

if (1023 > port) and (port > 49152):
    port = 9090
    
sock.connect((host, port))

print('Для выхода введите команду "exit".')

msg = ''

while msg != 'exit':
    msg = input('Введите сообщение:')
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()
