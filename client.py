import socket
def LogIn(sock):
     txt = sock.recv(1024).decode()
     passwd = input(txt)
     sock.send(passwd.encode())

try:
    port=int(input("ваш порт:"))
    if not 0 <= port <= 65535:
        raise ValueError
except ValueError :
    port = 9090

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', port))
user = sock.recv(1024).decode()
if "неизвестный" in user:
    name = input(user)
    sock.send(name.encode())
    LogIn(sock)
else:
    passwd = input(user)
    sock.send(passwd.encode())
msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    #print(msg)
    msg = input()

sock.close()