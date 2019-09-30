import socket
import re
from time import sleep



while True:
    port = input('Введите номер порта или нажмите enter для значиния по умолчанию: ')
    if port == '':
        port = 9090
        break
    elif not port.isnumeric():
        print('порт указан неверно')
    elif not 1024 < int(port) <= 65535:
        print ('попробуйте другой порт')
    else:
        port = int(port)
        break
while True:
    host = input('Введите адрес хоста или нажмите enter для значения по умолчанию: ')
    if host == '':
        host = 'localhost'
        break
    elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', host) == None:
        print('попробуйте другой адрес хоста')
    else:
        break

sock = socket.socket()
sock.setblocking(1)
sock.connect((host, port))

#msg = input()
msg = "exi"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
