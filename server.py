import socket

while True:
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    data=list()
    while True:
        msg = conn.recv(1024)
        if msg:
            data.append(msg.decode())
            print(data[-1])
        else:
            conn.close()
            break