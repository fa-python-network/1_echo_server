import socket

sock = socket.socket()
sock.bind(('', 7003))
print("Server starts")
sock.listen(0)

print("Now listen")

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg += data.decode()
    conn.send(data)

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
