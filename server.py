import socket
import logging
from validator import port_validation

DEFAULT_PORT = 9090

# Настройки логирования
logging.basicConfig(filename='server.log',filemode='w', format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

class Server:
    def __init__(self, port_number: int) -> None:
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
    port_flag = port_validation(port_input, check_open=True)
    if not port_flag:
        port_input = DEFAULT_PORT
        print(f"Выставили порт {port_input} по умолчанию")

    server = Server(int(port_input))


if __name__ == "__main__":
    main()
