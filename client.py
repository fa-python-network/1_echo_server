import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9091))

msg = ""
while True:
        client_input=input()
        if client_input=="exit":
                    break
        msg+=client_input
sock.send(msg.encode())

data = sock.recv(1024)
host=input()
hostlt=host.split(".",4)
for i in hostlt:
	if 0<=int(i)<=255:
		pass
	else
		host='localhost'
port=input()
if 1024 <=int(port)<=65535:
	pass
else:
	port=9091

sock.close()

print(data.decode())

