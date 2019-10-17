import socket


def msg_s(msg, conn):
    length_msg = str(len(msg))
    length_msg = '0' * (10 - len(length_msg)) + length_msg
    msg = length_msg + msg
    conn.send(msg.encode())


def msg_r(conn):
    try:
        length_msg = int(conn.recv(10).decode())
    except ValueError:
        msg = None
    else:
        msg = conn.recv(length_msg).decode()
    return msg


try:
    file = 'log_file_server.txt'
    sock = socket.socket()

    port = 9090

    while True:
        try:
            sock.bind(('', port))
        except:
            port += 1
        else:
            with open(file, 'a') as f:
                f.write('Запуск сервера\n')
            break

    sock.listen(1)
    with open(file, 'a') as f:
        f.write(f'Начало прослушивания порта {port}\n')
    print(f'Слушаю порт с номером {port}')

    try:
        with open('users.txt', 'r') as users:
            users = eval(users.read())
    except FileNotFoundError:
        with open('users.txt', 'w') as users:
            users = {}
    except SyntaxError:
        users = {}

    while True:
        conn, addr = sock.accept()
        addr = addr[0]

        try:
            if addr not in users.keys():
                flag = '1'
                msg_s(flag, conn)
                name = msg_r(conn)
                password = msg_r(conn)
                users[addr] = users.get(addr, [name, password])
                with open('users.txt', 'w') as u:
                    print(users, file=u)
            else:
                flag = '0'
                msg_s(flag, conn)
                passwd = users[addr][1]
                password = msg_r(conn)
                while True:
                    if passwd == password:
                        msg_s('0', conn)
                        msg_r(conn)
                        break
                    else:
                        msg_s('1', conn)
                        password = msg_r(conn)
            msg = 'Hello ' + users[addr][0]
            msg_s(msg, conn)

            with open(file, 'a') as f:
                f.write(f'Подключился клиент с {addr}\n')

            while True:
                data = msg_r(conn)
                with open(file, 'a') as f:
                    f.write(f'Получаю данные от {addr}\n')
                if not data:
                    with open(file, 'a') as f:
                        f.write(f'{addr} отключился\n')
                    conn.close()
                    break

                msg_s(data, conn)
                with open(file, 'a') as f:
                    f.write(f'Отправляю данные {addr}\n')
        except ConnectionResetError:
            continue

except KeyboardInterrupt:
    with open(file, 'a') as f:
        f.write('Закрытие сервера')
    sock.close()
