import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

msg = ""
input_date = input()
while input_date != "exit":
    msg += input_date
    input_date = input()

if msg != "":
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()


