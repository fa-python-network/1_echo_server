import socket
import logging
import json
import hashlib

with open("users.json", "r") as users_file:
    users = dict(json.load(users_file))

server_logger = logging.getLogger("server_logger")
log_handler = logging.FileHandler(filename="server_log.log", encoding="UTF-8")
log_handler.setLevel(logging.INFO)
server_logger.addHandler(log_handler)
server_logger.setLevel(logging.INFO)

sock = socket.socket()
default_port = 9090
while True:
    try:
        port = int(input("Введите порт на котором хотите меня поднять: "))
        if port > 65535 or port < 0:
            print("Порт должен быть числом в диапазоне 0-65535")
        else:
            break
    except TypeError:
        print("Порт должен быть числом в диапазоне 0-65535")

try:
    sock.bind(('', port))
except ConnectionError:
    print("Похоже, к этому порту нельзя причалиться =( пробую поискать другой . . .")
    try:
        for i in range(8080, 65535):
            print(f"Пробуем забиндить порт {i}")
            sock.bind(('', i))
            break
    except ConnectionError:
        print("Занято...")

sock.listen(0)

server_logger.info("Сервер поднят!")
while True:
    conn, addr = sock.accept()
    server_logger.info(f"{addr} подключился к серверу!")
    conn.send("Введите логин".encode())
    login = conn.recv(512).decode()
    if login in users:
        while True:
            conn.send("Введите пароль".encode())
            password = hashlib.md5(conn.recv(1024)).hexdigest()
            if password == users[login]:
                server_logger.info(f"Клиент {login} вошел")
                break
            conn.send("Попробуйте ещё раз".encode())
    else:
        conn.send("Введите логин для регистрации".encode())
        login = conn.recv(1024).decode()
        conn.send("Введите пароль".encode())
        password = hashlib.md5(conn.recv(1024)).hexdigest()
        users[login] = password
        server_logger.info(f"Клиент {login} зарегистрировался")
        with open("users.json", "w") as f:
            json.dump(users, f)

    msg = ''
    conn.send(f"Приветствую, {login}".encode())
    while True:
        try:
            data = conn.recv(1024)
        except ConnectionError:
            server_logger.info(f"{addr} разорвал соединение")
            break
        if not data:
            break
        msg += data.decode()
        server_logger.info(f"{addr} прислал сообщение: {msg}")
        conn.send(data)
        server_logger.info(f"Ответ клиенту {addr} отправлен")

    conn.close()
    server_logger.info(f"{addr} отключился")
