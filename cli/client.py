import socket
from cli_validator import port_validation, ip_validation

DEFAULT_PORT = 9090
DEFAULT_IP = "127.0.0.1"
END_MESSAGE_FLAG = "END_MESSAGE_FLAG"


class Client:
    def __init__(self, server_ip: str, port_number: int) -> None:
        sock = socket.socket()
        sock.setblocking(1)
        sock.connect((server_ip, port_number))
        self.sock = sock
        # Работа с данными, поступающими от пользователя
        self.user_processing()
        # Закрываем сокет
        self.sock.close()

    def send_message(self, message : str):
        """Отправка сообщения"""
      
        #Добавляем флаг конца сообщения (по-другому я не знаю как передавать больше 1024 и не разрывать соединение)
        message += END_MESSAGE_FLAG

        # Отправляем сообщение
        self.sock.send(message.encode())
        # Получаем ответ

        data = ""
        while True:
            # Получаем данные и собираем их по кусочкам
            chunk = self.sock.recv(1024)
            data += chunk.decode()

            #Если это конец сообщения, то значит, что мы все собрали и можем обратно отдавать клиенту
            if END_MESSAGE_FLAG in data:
                data = data.replace(END_MESSAGE_FLAG,"")
                
                print(f"Получили сообщение -> {data}")
                break

    def user_processing(self):

        while True:
            msg = input("-> ")
            # Если сообщение exit
            if msg == "exit":
                break

            self.send_message(msg)


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
