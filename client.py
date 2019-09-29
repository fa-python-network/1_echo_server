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

sock.close()

print(data.decode())
