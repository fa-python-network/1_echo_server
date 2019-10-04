import socket
import json
import hashlib

SALT = 'rnjrenfrenfer'.encode('utf-8')

with open('data.json', 'r') as f:
    datafile = json.load(f)


def pass_hash(passw):
    return hashlib.sha3_512(passw.encode('utf-8') + SALT).hexdigest()


f = open('log.txt', 'w')

sock = socket.socket()
port = 9090

while True:
    try:
        if port == 65536:
            print('Все порты заняты', file=f)
            break
        sock.bind(('', port))
        break
    except ConnectionResetError:
        port += 1

user = ''
print('Сервер запущен', file=f)
print(f'Прослушиваемый порт: {port}', file=f)
sock.listen(0)
print('Сервер прослушивается', file=f)

while True:
    conn, addr = sock.accept()
    msg = ''

    client = addr[0]
    conn.send(addr[0].encode())

    if client in datafile.keys():
        conn.send('1'.encode())
        print('Пользователь найден в базе', file=f)
        nick = datafile[client]["name"]
        password = datafile[client]["password"]
        check = conn.recv(1024).decode()
        if pass_hash(check) == password:
            conn.send('1'.encode())
            print('Пароль прошел проверку', file=f)
        else:
            conn.send('0'.encode())
            print('Пароль не прошел проверку', file=f)

    else:
        conn.send('0'.encode())
        print('Пользователь не найден в базе, запись нового', file=f)
        user = 'new'
        nick = conn.recv(1024).decode()
        password = pass_hash(conn.recv(1024).decode())

    try:
        while True:
            data = conn.recv(1024)
            print('Принят поток данных', file=f)
            if not data:
                break
            msg += data.decode() + ' '
            conn.send(data)
            print('Данные обработаны и отправлены клиенту', file=f)
    except ConnectionAbortedError:
        datafile[client] = {}
        datafile[client]['ip'] = addr[0]
        datafile[client]['port'] = port
        datafile[client]['name'] = nick
        datafile[client]['password'] = password

        print('Информация о клиенте сохранена', file=f)

        with open('data.json', 'w') as file:
            json.dump(datafile, file)
        conn.close()
        print('Связь с клиентом оборвана', file=f)
        command = input('Если вы хотите остановить сервер введите: "stop"\n ')
        if command == 'stop':
            sock.close()
            print('Сервер остановлен', file=f)
            f.close()
            break
