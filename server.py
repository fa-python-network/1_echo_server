import json

from socket import socket, SO_REUSEADDR, SOL_SOCKET
from asyncio import Task, get_event_loop
from threading import Thread
from datetime import datetime


class Loger(Thread):
    """
    Логер в отдельном потоке
    """

    def __init__(self, host: str, port: int, file_name: str = "logs.log"):
        """
        Конструктор логера

        :param file_name:
        :param host:
        :param port:
        """

        Thread.__init__(self)
        self.file_name = file_name
        self.host = host
        self.port = port

    def write_to_file(self, data: str, file_name: str = None):
        """
        Пишет данные в файл

        :param data:
        :param file_name:
        :return:
        """

        if file_name is None:
            file_name = self.file_name

        with open(file_name, "a", encoding="utf-8") as file_one:
            print(data, file=file_one)

        return data

    def run(self):
        """
        Срабатывает автоматический при запуске логера

        :return:
        """

        return self.info_log("Логер запущен")

    def info_log(self, text: str):
        """
        Лог информации

        :param text:
        :return:
        """

        text = f"{self.today()} – INFO – {text}"
        print(self.write_to_file(text))

    def server_is_running(self):
        """
        Запуск сервера

        :return:
        """

        return self.info_log(f"Сервер {self.host}:{self.port} запущен")

    def server_is_stopped(self):
        """
        Остановка сервера

        :return:
        """

        return self.info_log("Сервер остановлен")

    def start_listening_port(self, port):
        """
        Начало прослушивания порта

        :param port:
        :return:
        """

        return self.info_log(f"Запущено пропуслушивание порта {port}")

    def new_connection(self, user: tuple):
        """
        Новое подключение

        :return:
        """

        return self.info_log(f"Пользователь {user[0]}:{user[1]} подключен")

    def connection_closed(self, user: tuple):
        """
        Закрытие соединения

        :return:
        """

        return self.info_log(f'Пользователь {user[0]}:{user[1]} отключился')

    def socket_closed_other_side(self, user):
        """
        Сокет был закрыт другой стороной

        :return:
        """

        return self.info_log(f"Пользователь {user[0]}:{user[1]} попросил попросил закрыть его сокет")

    def send_data(self, user: tuple, data: str):
        """
        Отправка данных сервером

        :param user:
        :param data:
        :return:
        """

        return self.info_log(f"Сервер отправил сообщение «{data}» пользователю {user[0]}:{user[1]}")

    def obtain_data(self, user: tuple, data: str):
        """
        Получение данных

        :param user:
        :param data:
        :return:
        """

        return self.info_log(f"Пользователь {user[0]}:{user[1]} прислал «{data}»")

    @staticmethod
    def today():
        """
        Возвращает текущий день

        :return:
        """

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Peer(object):
    ENCODING = "utf-8"
    BUFFER_SIZE = 1024

    def __init__(self, sock_server: 'Server', sock: socket, address: tuple, loger: Loger):
        """
        Конструктор сокета

        :param sock_server:
        :param sock:
        :param address:
        """

        self.loop = sock_server.loop
        self.address = address
        self.loger = loger
        self._sock = sock
        self._server = sock_server
        Task(self._peer_handler())

    async def send(self, data):
        """
        Отправляет данные текущему сокету

        :param data:
        :return:
        """

        await self.loop.sock_sendall(self._sock, data.encode(self.ENCODING))

    async def _peer_handler(self):
        """
        Получает новых данных для сокета экземлпляра текущего класса

        :return:
        """

        try:
            await self._peer_loop()
        except IOError:
            pass
        finally:
            self._server.peer_remove(self)

    async def _peer_loop(self):
        """
        Получает сообщение пользователя

        :return:
        """

        while True:
            data = await self.loop.sock_recv(self._sock, self.BUFFER_SIZE)
            if data == b"":
                break
            data = data.decode(self.ENCODING)
            self.loger.obtain_data(self.address, data)
            if data == "exit":
                self.loger.socket_closed_other_side(self.address)
                self._server.peer_remove(self)
            elif self._server.db[self.address[0]] is None:
                self._server.db.update({self.address[0]: data})
                await self.send(f"Запомнили ваше имя, {data}")


class Server(object):

    def __init__(self, host: str = "localhost", port: int = 9090, listen: int = 100):
        """
        Конструктор сервера

        :param host:
        :param port:
        :param listen:
        """

        self.loop = get_event_loop()
        self._server_sock = socket()
        self._server_sock.setblocking(False)
        self._server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self._server_sock.bind((host, port))
        self._server_sock.listen(listen)
        self.loger = Loger(host, port)
        self.loger.run()
        self._users = list()
        self.db = self.open_file()
        Task(self._server())
        self.loger.server_is_running()
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.loger.server_is_stopped()
            self.close_file()

    def open_file(self, file_name: str = "db.json") -> dict:
        """
        Открывает файл

        :param file_name:
        :return:
        """
        try:
            open(file_name)
        except (FileNotFoundError, IOError):
            self.close_file({})
        with open(file_name, 'r', encoding='utf-8') as file_one:
            return json.load(file_one)

    def close_file(self, data: dict = None, file_name: str = "db.json"):
        """
        Открывает файл

        :param data:
        :param file_name:
        :return:
        """

        with open(file_name, 'w', encoding='utf-8') as file_one:
            json.dump(self.db if data is None else data, file_one, ensure_ascii=False, sort_keys=False, indent=4)

    def peer_remove(self, peer: Peer):
        """
        Удаляет прослушиваемый сокет из сервера

        :param peer:
        :return:
        """

        self._users.remove(peer)
        self.loger.connection_closed(peer.address)

    async def _server(self):
        """
        Принимает новые соединения с серверного сокета

        :return:
        """

        while True:
            user_sock, client = await self.loop.sock_accept(self._server_sock)
            user_sock.setblocking(False)
            user = Peer(self, user_sock, client, self.loger)
            self._users.append(user)
            self.loger.new_connection(user.address)
            if user.address[0] in self.db:
                if self.db[user.address[0]] is None:
                    message = "Привет! Прошлый раз ты так и не отправил свое имя. Пришли свое имя :)"
                else:
                    message = f"Привет {self.db[user.address[0]]}"
            else:
                self.db.update({user.address[0]: None})
                message = f"Привет! Давай знакомиться! Пришли свое имя"
            print(self.db)
            await user.send(message)
            self.loger.send_data(user.address, message)


class Ports(socket):

    def __init__(self, host: str = "localhost", min_port: int = 9090, max_port: int = 9100):
        """
        Конструктор проверки портов

        :param host:
        :param min_port:
        :param max_port:
        """
        super(Ports, self).__init__()
        self.host = host
        self.min_port = min_port
        self.max_port = max_port
        self.free_port = self.__free_port()

    def select_port(self):
        """
        Выбор свободного порта

        :return:
        """

        port = self.free_port
        if port is None:
            while True:
                port = input("Не нашли свободный порт в заданном диапазоне\nВведите порт, который требуется запустить "
                             "насильно: ")
                if port.isdigit():
                    port = int(port)
                    if 1 <= port <= 65535:
                        return port
        else:
            return port

    def __free_port(self):
        """
        Ищет свободный порт в заданном диапазоне

        :return:
        """

        for port in range(self.min_port, self.max_port):
            try:
                self.bind((self.host, port))
                self.close()
                return port
            except OSError:
                pass
        return None


if __name__ == '__main__':
    # Это для будущих поколений(4 задание), я думаю оно только мешает, ибо порт задается насольно, и я уверен,
    # что он свободен

    # answer = input("Хотите ввести адрес хоста?  ")
    # if answer.lower() == "y":
    #     answer = input("Введите адрес хоста")
    # else:
    #     answer = "localhost"
    # Тоже самое про порт :/
    # server = Server(host=answer, port=Ports().select_port())
    # Написано за 1 час, 30 минут

    # server = Server(port=9090)
    server = Server(port=Ports().select_port())
