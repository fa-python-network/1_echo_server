import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)


while True:
    conn, addr = sock.accept()
    print(f'Клиент {addr} подключился к серверу')
    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += ' ' + data.decode()
        conn.send(data)
        

    conn.close()
    print('Соединение завершено')
