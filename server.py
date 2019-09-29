import socket
from re import match
sock = socket.socket()
host = 'localhost'
port = 9090
host_ = input('Host: ')	
port_ = input('Port:')
host_regex = r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]'
if host_ and match(host_regex, host_):
    host = host_
print(f'current host:{host}')
if port_.isdigit() and  1024<=int(port_)<=65535:
	port = int(port_)
print(f'current port: {port}')
sock.bind(("",9094))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    print(addr)
    msg =''
    data = conn.recv(1024)
    print(f'Data: {data.decode()}')
    msg = data.decode()    
    print(f'MSG: {msg}')
    conn.send(msg.encode())
    conn.close()
