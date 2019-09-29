import socket

sock = socket.socket()
sock.bind(('', 9091))
print("Server starts")
sock.listen(0)
print("Now listen")

while True:
    conn, addr = sock.accept()
    print("new connection: " + f"{addr}")

    msg = ''

    while True:
        data = conn.recv(1024)
        print("new data from client")
        if not data:
            break
        msg += data.decode()
        conn.send(data)
        print("data to client")

    print(msg)

    conn.close()
    print('stop client')
