import socket
from time import sleep
import re
while True:
    inputPort = input('Vvedite port nomber or \'Ok\' if you want port 9090: ')
    if inputPort == 'Ok':
        print('Ok')
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
    inputHost = input('Vvedite host or \'Ok\' if you want localhost: ')
    if inputHost == 'Ok':
        print('Ok')
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
data = b''
while True:
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
