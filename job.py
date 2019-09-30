import socket

sock = socket.socket()
sock.bind(("", 9093))
sock.listen(1)

conn, addr = sock.accept()
print(addr)

data=conn.recv(1024)
print(data.decode())

conn.send(b"hi")
conn.send(('\nIP {}'.format(addr[0])).encode())

sock.close()
