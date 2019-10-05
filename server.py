import socket

sock = socket.socket()

print ("Select port number")
portnum = int(input())

while True:

    try:
        sock.bind(('', portnum))
        break

    except:
        portnum += 1

while True:

    sock.listen(1)
    conn, addr = sock.accept()
    print(addr)

    while True:

        msg = ''

        try:
            data = conn.recv(1024)
            msg += data.decode()
            conn.send(data)

        except:
            break

        print(msg)

    conn.close()
