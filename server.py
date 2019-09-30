import socket
f = open ('log.txt', 'w')
sock = socket.socket()
freeHost = 1025
while True:
    try:
        if freeHost == 65536:
            print('All ports busy')
            break
        sock.bind(('', freeHost))
        break
    except:
        freeHost += 1
print(freeHost)
print("Server starts", file = f)
print("Server starts")
sock.listen(0)
print("Now listen", file = f)

while True:
    conn, addr = sock.accept()
    print("connection: " + f"{addr}", file = f)

    msg = ''
    e = ''

    while True:

        data = conn.recv(1024)
        print("new data from client", file = f)
        if not data:
            break
        msg += data.decode()
        conn.send(data)
        print("data to client", file = f)


    print(msg)

    conn.close()
    print('stop client', file = f)
    e = input('To stop vvevide \'stop\' if not something else: ')
    if e == 'stop':
        sock.close()
        print('server stop', file = f)
        f.close()
        break


