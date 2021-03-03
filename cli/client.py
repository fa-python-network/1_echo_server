import socket
import json
import logging
from cli_validator import port_validation, ip_validation

DEFAULT_PORT = 9090
DEFAULT_IP = "127.0.0.1"
END_MESSAGE_FLAG = "CRLF"

# Настройки логирования
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    handlers=[logging.FileHandler("./logs/client.log"), logging.StreamHandler()],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class Client:
    def __init__(self, server_ip: str, port_number: int) -> None:
        sock = socket.socket()
        sock.setblocking(1)
        sock.connect((server_ip, port_number))
        self.sock = sock
        logging.info(f"Успешное соединение с сервером {server_ip}:{port_number}")
        
        #Авторизуемся
        self.send_auth()
        # Работа с данными, поступающими от пользователя
        self.user_processing()
        # Закрываем сокет
        self.sock.close()

    def send_auth(self):
        """
        Логика авторизации клиента
        """

        exit_flag = True
        while exit_flag:
            user_password = input("Введите пароль авторизации -> ")
            if user_password != "":

                data = json.dumps({"password" : user_password}, ensure_ascii=False)
                # Отправляем сообщение
                self.sock.send(data.encode())
                logger.info(f"Отправка данных серверу: '{data}'")
                #Получаем данные с сервера
                result = json.loads(self.sock.recv(1024).decode())["result"]
                if result:
                    print("Авторизация прошла успешно")
                    break

                print("Неверный пароль!")

            else:
                print("Пароль не может быть пустым")


        #Если нет такого пользователя - надо зарегаться
        #if result == False:

        

    def send_message(self, message: str):
        """Отправка сообщения"""

        # Добавляем флаг конца сообщения (по-другому я не знаю как передавать больше 1024 и не разрывать соединение)
        message += END_MESSAGE_FLAG

        # Отправляем сообщение
        self.sock.send(message.encode())
        logger.info(f"Отправка данных серверу: '{message}'")
        # Получаем ответ

        data = ""
        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = self.sock.recv(1024)
            data += chunk.decode()

            # Если это конец сообщения, то значит, что мы все собрали и можем обратно отдавать клиенту
            if END_MESSAGE_FLAG in data:
                logger.info(f"Прием данных от сервера: '{data}'")
                data = data.replace(END_MESSAGE_FLAG, "")
                break

            # Если приняли часть данных - сообщаем
            else:
                logger.info(f"Приняли часть данных от сервера: '{data}'")

    def user_processing(self):

        while True:
            msg = input("-> ")
            # Если сообщение exit
            if msg == "exit":
                break

            self.send_message(msg)

    def __del__(self):
        logger.info("Разрыв соединения с сервером")


def main():

    port_input = input("Введите номер порта сервера -> ")
    port_flag = port_validation(port_input)
    # Если некорректный ввод
    if not port_flag:
        port_input = DEFAULT_PORT
        print(f"Выставили порт {port_input} по умолчанию")

    ip_input = input("Введите ip-адрес сервера -> ")
    ip_flag = ip_validation(ip_input)
    # Если некорректный ввод
    if not ip_flag:
        ip_input = DEFAULT_IP
        print(f"Выставили ip-адрес {ip_input} по умолчанию")

    client = Client(ip_input, int(port_input))


if __name__ == "__main__":
    main()
