import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
con, addr = sock.accept()
print(addr)

msg = ''
logf = open("ser.log", "_")

sock = socket.socket()
sock.bind(("", 9094))
sock.listen(5)

while True:
    data = con.recv(1024)
    if not data:
        break
    msg += data.decode()
    con.send(data)

print(msg)

con.close()
con, addr = sock.accept()
print(addr)
msg = ''
while True:
    data = con.recv(1024)
    if not data:
        break
    logf.write('Data: {data.decode()}')
    msg = data.decode()
    logf.write(('Message: {msg}'))
    con.send(msg.encode())
con.close()
logf.close()
