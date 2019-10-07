import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))

msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)
print('Put hostname:')
hostname = input()
print('Put Port:')
port = input()

sock.close()
if int(port) > 1024 and int(port) < 65000:
            port1 = int(user_port)
else:
            port1 = 9094

print(data.decode())
sock.connect((hostname, port1))
msg = "Hi!"
while True:
    mess = input()
    print('Your message: {mess}')
    sock.send(mess.encode())
    data = sock.recv(1024)
    print(data.decode())
    if mess == 'exit':
        print('exit')
        sock.close()
        break
