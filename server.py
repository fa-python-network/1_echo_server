import socket

port =  int(input("Порт:"))
port = port if (port >= 0 and port <= 65535)  else  9090
while True:
    sock = socket.socket()
    sock.bind(('', port))
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