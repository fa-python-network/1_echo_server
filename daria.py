import socket

sock = socket.socket()
sock.bind(("",9095))
sock.listen(1)

conn, addr = sock.accept()
print(addr)

data = conn.recv(1024)
print(data)

conn.send(b'Hi, client\n')
conn.send(('your IP is {}'.format(addr[0])).encode())

sock.close()
