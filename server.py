import socket
import logging
import json
import hashlib
import binascii
import os


def hash_password(password: str) -> str:
    """
    Функция хэширования паролей
    :param password:
    :return hash password:
    """
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Сравнение введенного пароля и хранящегося хэша
    :param stored_password:
    :param provided_password:
    :return:
    """
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512',
        provided_password.encode('utf-8'),
        salt.encode('ascii'),
        100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def connection_with_auth(sock):
    """
    Функция предоставления подключения пользователя с авторизацией
    :param sock:
    :return:
    """
    conn, addr = sock.accept()
    address = ':'.join([str(i) for i in addr])
    if address in data_users['users']:
        conn.send(f"Добрый день {data_users['users'][address]['name']}".encode())
        while True:
            conn.send("Введите пароль".encode())
            data_password = conn.recv(1024)
            if not data_password:
                conn.send(f"Пароль введен неверно".encode())
            else:
                if verify_password(data_users['users'][address]['password'], data_password):
                    conn.send(f"Пароль введен верно".encode())
                    break
                else:
                    conn.send(f"Пароль введен неверно".encode())
    else:
        conn.send(f"Введите ваше имя!".encode())
        data_name = conn.recv(1024).decode()
        conn.send(f"Введите пароль!".encode())
        data_pass = conn.recv(1024).decode()
        if not data_name or not data_pass:
            conn.send(f"Имя или пароль введены некорректно. До свидания!".encode())
            return None, None
        data_users['users'][address] = {'name': data_name, 'password': hash_password(data_pass)}
        with open('data_users.json', 'w') as file:
            json.dump(data_users, file)
        conn.send(f"Добро пожаловать {data_name}. Ваш пароль успешно добавлен".encode())
        return conn, address


# Открытие файла с информацией о пользователях. Если он отсутствует, создается новый
try:
    with open("data_users.json", "r") as read_file:
        data_users = json.load(read_file)
except FileNotFoundError:
    data_users = {'users': {}}
    with open('data_users.json', 'w') as file:
        json.dump(data_users, file)

#  Создается и используется объект логгирования
logger = logging.getLogger("serverLogger")  # Создает объект логгирования
logger.setLevel(logging.INFO)  # Установка уровня логгирования
fh = logging.FileHandler("server.log")  # Файл логгирования
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Формат строчки лога
fh.setFormatter(formatter)  # Устанавливает форматирование к файлу
logger.addHandler(fh)  # Добавление хэндлера форматирования к объекту логгирования

logger.info("Start server")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 0))
sock.listen(1024)
print(f'Bind to  {sock.getsockname()[1]} port')
logger.info(f"Bind to {':'.join([str(i) for i in sock.getsockname()])}")

conn, addr = connection_with_auth(sock)
logger.info(f"Connect client {addr[0]}:{addr[1]}")
print(addr)

msg = ''

while True:
    try:
        data = conn.recv(1024)
        if not data:
            conn, addr = connection_with_auth(sock)
        elif data == 'exit':
            logger.info(f"Disconnect client {addr[0]}:{addr[1]}")
            conn.close()
        else:
            logger.info(f"From client {addr[0]}:{addr[1]} - {data}")
            conn.send(data.upper())
    except ConnectionResetError:
        conn, addr = connection_with_auth(sock)

sock.close()