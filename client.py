import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

print('Put hostname:')
 hostname = input()
 print('Put Port:')
 port = input()

if int(port) > 1024 and int(port) < 65000:
             port1 = int(user_port)
         else:
             port1 = 9094

sock.connect((hostname, port1))
msg = "Hi!"
while True:
    mess = input()
    print(f'Your message: {mess}')
    sock.send(mess.encode())
    data = sock.recv(1024)
    print(data.decode())
    if mess == 'exit':
        print('exit')
        sock.close()
        break
