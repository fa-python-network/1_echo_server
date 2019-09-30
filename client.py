import socket
from time import sleep
import re
while True:
    inputPort = input('Vvedite port nomber or \'ok\' if you want port 9090: ')
    if inputPort == 'ok':
        print('ok')
        inputPort = 9090
        break
    elif not inputPort.isnumeric():
        print('try again')
    elif not  1024 < int(inputPort) <= 65535:
        print('try again')
    else:
        inputPort = int(inputPort)
        print('great')
        break
while True:
    inputHost = input('Vvedite host or \'ok\' if you want localhost: ')
    if inputHost == 'ok':
        print('ok')
        inputHost = 'localhost'
        break
    elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', inputHost) == None:
       print('try again')
    else:
        break
sock = socket.socket()
sock.setblocking(1)
sock.connect((inputHost, inputPort))
print("Connection with server")
aut = sock.recv(1024).decode()
print(aut)
if aut == 'Hello, You\'re new, please enter you name ': #регистрация нового пользователя
    sock.send(input().encode())
    print(sock.recv(1024).decode())
    sock.send(input().encode())
else: #ввод пароля
    sock.send(input().encode())
aut = sock.recv(1024).decode()
print(aut)
data = b''
while aut != 'It\'s Not Correct':
    msg = input("Vvedite: ")
    if msg == "exit":
        sock.close()
        print('stop connection')
        break
    sock.send(msg.encode())
    print('send data to server')
    data += sock.recv(1024)
    print('new data from server')

if data:
    print(data.decode())
