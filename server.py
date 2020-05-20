import socket
import logging

logging.basicConfig(
    filename='history.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.DEBUG
)

logging.debug('-----------------------------------')
logging.debug('Сервер запущен')

sock = socket.socket()  # инициализация сокета
sock.settimeout(60)

# Задаётся базовый порт
while True:
    try:
        while True:
            port = int(input("Введите порт (диапозон 1024-65535): "))
            if 1024 <= port <= 65535:
                break
    except ValueError:
        print("Повторите ввод!")
    else:
        break

# Проверка доступности порта. Перебор, в случае неудачи
while True:
    try:
        sock.bind(('', port))
    except socket.error:
        logging.warning('Порт %s занят, поиск другого', port)
        port += 1
        if port > 65535:
            logging.warning('Достигнут предел диапозона портов')
            port = 1024
    else:
        logging.debug('Назначен порт %s', port)
        break

logging.debug('Прослушивание порта')
sock.listen(1)

while True:

    logging.debug('Ожидание подключения клиента')
    try:
        conn, addr = sock.accept()
    except socket.timeout:
        try:
            logging.warning('Сервер бездействует, остановка ..')
            sock.shutdown(socket.SHUT_RDWR)
        except (socket.error, OSError, ValueError):
            pass
        break

    logging.debug('Клиент подключен, информация о нём: %s', addr)

    logging.debug('Обмен сообщениями с клиентом')
    while True:
        data = conn.recv(1024)
        if not data or data.decode() == "exit":
            logging.debug('Клиент завершил обмен')
            break
        logging.debug('Сообщение от %s: %s', addr, data.decode())
        conn.send(data)

    conn.close()
    logging.debug('Клиент отключен')

sock.close()
logging.debug('Сервер остановлен')
