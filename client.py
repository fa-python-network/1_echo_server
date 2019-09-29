import socket
import re
from time import sleep

while True:
    port = input('Введите порт от 1024 до 65535: \n')
    if not port.isnumeric():
        print('Ошибка')
    elif 1023 <= int(port) <= 65535:
        break
    else:
        print('Ошибка: порт не входит в нужный диапазон')

while True:
    ip = input('Введите ip сервера или оставьте пусстым для значения localhost: \n')
    if ip == '':
        ip = 'localhost'
        break
    elif re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip) == None:
        print('Ошибка')
    else:
        break
    
sock = socket.socket()
sock.setblocking(1)
sock.connect((ip, int(port)))

while True:
    msg = input("Input message: ")
    if msg == "exit":
        sock.close()
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
