import socket
import logging
import random
from server_validator import port_validation, check_port_open
import yaml
from typing import Dict
from data_processing import DataProcessing

END_MESSAGE_FLAG = "END_MESSAGE_FLAG"
DEFAULT_PORT = 9090

# Настройки логирования
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
        handlers=[
        logging.FileHandler("./logs/server.log"),
        logging.StreamHandler()
    ],
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
            #Новое соединение
            conn, addr = self.sock.accept()
            #self.login_logic
            logging.info(f"Новое соединение от {addr}")
            self.message_logic(conn, addr)

    #def login_logic
    def message_logic(self, conn, addr):
        """
        Обмен сообщениями (когда уже успешно авторизовались)
        """

        data = ""
        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = conn.recv(1024)
            data += chunk.decode()

            print(data)
            #Если это конец сообщения, то значит, что мы все собрали и можем обратно отдавать клиенту
            if END_MESSAGE_FLAG in data:
                data = data.replace(END_MESSAGE_FLAG,"")
                logging.info(f"Получили сообщение {data} от клиента: '{addr}'")
                conn.send(data.encode())
                print(f'{data.encode()} было отправлено обратно клиенту')
                data = ""

            #Если вообще ничего не пришло - это конец всего соединения
            if not chunk:
                break

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
