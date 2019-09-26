import socket

try:
    port=int(input("ваш порт:"))
    if not 0 <= port <= 65535:
        raise ValueError
except ValueError :
    port = 9090

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', port))
msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    #print(msg)
    msg = input()

sock.close()
