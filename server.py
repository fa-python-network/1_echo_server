import socket
import logging

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

    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        server_logger.info(f"{addr} прислал сообщение: {msg}")
        conn.send(data)
        server_logger.info(f"Ответ клиенту {addr} отправлен")

    conn.close()
    server_logger.info(f"{addr} отключился")
