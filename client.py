import socket
sock = socket.socket()
sock.connect(('localhost',9094))
msg = "Hello, server!"
while True:
    mess = input()
    print(f'MSG: {mess}')
    sock.send(mess.encode())
    data = sock.recv(1024)
    print(data.decode())
    if mess == 'exit':
        print('Got exit')
        sock.close()
        break
 
