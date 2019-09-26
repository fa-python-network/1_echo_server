from socket import socket
from threading import Thread


class Client(socket):
    BUFFER_SIZE = 1024
    ENCODING = 'utf-8'

    def __init__(self, host: str = "localhost", port: int = 9090):
        """
        Конструктор клиента

        :param host:
        :param port:
        """

        super(Client, self).__init__()
        self.connect((host, port))
        self.listener_thread = Thread(target=self.listener)
        self.listener_thread.start()
        self.main_loop()

    def main_loop(self):
        try:
            while True:
                message = input('| ')
                self.send(message.encode(self.ENCODING))
        except EOFError:
            pass
        finally:
            self.close()

    def listener(self):
        try:
            no_data = 0
            while True and no_data <= 3:
                data = self.recv(self.BUFFER_SIZE).decode(self.ENCODING)
                if data == "":
                    no_data += 1
                else:
                    no_data = 0
                print(' *server* => ', data)
        except ConnectionAbortedError:
            pass


if __name__ == '__main__':

    # Тоже не удобно  :)

    # answer_host = input("Хотите ввести адрес хоста?  ")
    # if answer_host.lower() == "y":
    #     answer_host = input("Введите адрес хоста")
    # else:
    #     answer_host = "localhost"
    #
    # answer_port = input("Хотите ввести адрес хоста?  ")
    # if answer_port.lower() == "y":
    #     try:
    #         answer_port = int(input("Введите адрес хоста"))
    #     except ValueError:
    #         answer_port = 9090
    # else:
    #     answer_port = 9090
    #
    # client = Client(host=answer_host, port=answer_port)

    client = Client(port=9090)
