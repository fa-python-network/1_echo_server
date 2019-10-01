import hashlib
import random
import re

ENCODING = 'utf-8'
SALT = '//no_system_is_safe'.encode('utf-8')
COLORS = ['\33[31m', '\33[32m', '\33[33m', '\33[34m', '\33[35m', '\33[36m', '\33[91m', '\33[92m', '\33[93m', '\33[94m',
          '\33[95m', '\33[96m']
EMOJIS = {
    'airplane': '✈',
    'upside-down face': '🙃',
    'smile': '😊',
    'kiss': '😘',
    'ok': '👌',
    'sad': '☹'
}
EMOJIS_PATTERN = re.compile(r':([\w\s]+):')


class Security:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return hashlib.sha512(password.encode('utf-8') + SALT).hexdigest()

    @staticmethod
    def get_new_token() -> str:
        return hashlib.sha512(str(random.randint(-2147483648, 2147483647)).encode('utf-8') + SALT).hexdigest()


class SocketMethods:
    @staticmethod
    def receive_text(conn) -> str:
        msg_len = int(conn.recv(4), 16)
        return conn.recv(msg_len).decode(ENCODING)

    @staticmethod
    def send_text(conn, message: str):
        message = message.encode(ENCODING)
        msg_len = hex(len(message))[2:]
        msg_len = '0' * (4 - len(msg_len)) + msg_len
        msg_len = msg_len.encode(ENCODING)
        conn.send(msg_len + message)
