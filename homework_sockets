import socket
from time import sleep
from threading import Thread

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))

#msg = input()
msg = "Hi!"
while True:
    try:
        data = sock.recv(1024)
        msg = data.decode()
        print(msg)
    except:
        break

try:
    sock = socket.socket()
    print('Jot down host')
    host = input()
    print('Jot down  port')
    port = int(input())
    sock.connect((host, port))
except:
    host = 'localhost'
    port = 9095
    sock.connect((host, port))

print('Jot down passwd"')
passwd = input()
msg = passwd
sock.send(msg.encode())


import socket
import pickle

sock = socket.socket ( )
sock.bind((' ', 9090))
sock.listen(1)
conn, addr = sock.accept ( )

print (addr)

msg= conn.recv(1024)
print(msg)
conn.send(msg)
conn.close
 
import socket
import pickle

sock = socket.socket ( )
sock.connect(( ' localhost ' , 9090))
sock.send( ' hello, world! ' )

data = sock.recv(1024)
sock.close()

print data
