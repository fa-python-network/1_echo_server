import socket
import logging
import random
from server_validator import port_validation, check_port_open
import yaml
from typing import Dict
from data_processing import DataProcessing

DEFAULT_PORT = 9090

# Настройки логирования
logging.basicConfig(
    filename="./logs/server.log",
    filemode="w",
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class Server:
    def __init__(self, port_number: int) -> None:

        self.database = DataProcessing()

        sock = socket.socket()
        sock.bind(("", port_number))
        sock.listen(0)
        # Наш сокет
        self.sock = sock
        # Текущее соединение
        logging.info(f"Сервер инициализировался, слушает порт {port_number}")
        # Ожидаем новое подключение
        while True:
            conn, addr = self.sock.accept()
            self.new_connection(conn, addr)

    def new_connection(self, conn, addr):
        """
        Обработчик нового соединения
        """
        logging.info(f"Новое соединение от {addr}")
        msg = ""

        while True:
            # Получаем данные
            data = conn.recv(1024)

            # Если нет данных - больше ничего не ожидаем от клиента
            if not data:
                break

            msg += data.decode()
            conn.send(data)

            data_str = str(data, "utf-8")
            logging.info(f"Получили сообщение от клиента: '{data_str}'")

def main():

    port_input = input("Введите номер порта для сервера -> ")
    # Тут проверка на то, занят ли порт
    port_flag = port_validation(port_input, check_open=True)

    if not port_flag:

        # Если порт по-умолчанию уже занят, то перебираем свободные порты
        if not check_port_open(DEFAULT_PORT):
            print(
                f"Порт по умолчанию {DEFAULT_PORT} уже занят! Подбираем рандомный порт.."
            )
            stop_flag = False
            while not stop_flag:
                current_port = random.randint(49152, 65535)
                print(f"Сгенерировали рандомный порт {current_port}")
                stop_flag = check_port_open(current_port)

            port_input = current_port
        else:
            port_input = DEFAULT_PORT
        print(f"Выставили порт {port_input} по умолчанию")

    server = Server(int(port_input))


if __name__ == "__main__":
    main()
