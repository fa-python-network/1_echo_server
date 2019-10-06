import socket, errno
import sys

class Server(socket):
    """Сервер"""

    def __init__(self):
        """Создание сокета"""
        super().__init__()
        self.sock=soket.soket


    def send_msg(msg, sock):
        """Отправка сообщения с добавлением длины сообщения"""
        length_msg = str(len(msg))
        length_msg = '0'*(10-len(length_msg)) + length_msg
        msg = length_msg + msg
        sock.send(msg.encode())

    def recv_msg(sock):
        """Получение сообщения с учётом его длины"""
        length_msg = int(sock.recv(10).decode())
        msg = sock.recv(length_msg).decode()
        return msg


    def close_server():
        """Закрытие сервера, используется для добавления соответствующей
        записи в лог файл при закрытии сервера через Ctrl+C"""
	    with open ('log.txt', 'a') as file:
		    print('Остановка сервера', file=file)
	    global sock
	    sock.close()
	    sys.exit()

    def new_user(conn, addr, d):
        """Добавление нового пользователя в файл users.txt"""
        name = recv_msg(conn)
        send_msg('1', conn)
        password = recv_msg(conn)
        d[addr[0]] = d.get(addr[0], [name, password])
        with open ('users.txt', 'w') as users:
            print(d, file=users)


    def old_user(conn, addr, d):
        """Проверка пароля при входе старого пользователя"""
        passwd = d[addr[0]][1]
        password = recv_msg(conn)
        if passwd == password:
            send_msg('0', conn)
            recv_msg(conn)
            return
        else:
            send_msg('1', conn)
            old_user(conn, addr, d)
        
            

    def sha_podklyuchimsya(self):
        """Поиск незанятого порта и его прослушивание"""
        self.port = 9090
        flag = 1

        while flag:
            try:
                self.sock.bind(('', self.port))
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    self.port+=1
            else:
                flag = 0
        print(self.port)
        
        with open ('log.txt', 'a') as file:
		        print('Запуск сервера', file=file)




    def get_users(self):
        """Получение данных про всех старых клиентов"""
        #Пытаемся прочесть данные из файла и преобразовать их в словарь
        try:
            with open ('users.txt', 'r') as users:
                self.d = eval(users.read())
        #Если файла нет: создаём его, список юзеров - пустой словарь
        except FileNotFoundError:
            with open ('users.txt', 'w') as users:
                self.d={}
        #Если файл пустой: список юзеров - пустой словарь
        except SyntaxError:    
                self.d={}

    
    def proslushka_poshla(self):
        self.sock.listen(1)

        with open ('log.txt', 'a') as file:
	        print('Начало прослушивания порта', file=file)



    def connecting(self):
        """Подключение клиента"""
        while True:

            conn, addr = self.sock.accept()
            with open ('log.txt', 'a') as file:
                print('Подключение клиента', file=file)		
            
        #Считывание имени клиеента и пароля
            if addr[0] not in d.keys():
                flag = str(1)
                send_msg(flag, conn)
                new_user(conn, addr, d)
            else:
                flag = str(0)
                send_msg(flag, conn)
                old_user(conn, addr, d) 

            msg = 'Hello ' + d[addr[0]][0]
            send_msg(msg, conn)
        
            chatting(conn)

    def chatting(self, conn):
        """Обмен сообщениями с клиентом"""            
            while True:
                data = recv_msg(conn)
                with open ('log.txt', 'a') as file:
                    print('Приём данных от клиента', file=file)
                if not data:
                    conn.close()
                    break
                
                send_msg(data.upper(), conn)
                with open ('log.txt', 'a') as file:
                    print('Отправка данных клиенту', file=file)


            with open ('log.txt', 'a') as file:
                print('Отключение клиента', file=file)



    def main(self):
        """то, что нужно запустить для работы сервера"""
        sha_poodklyuchimsya()
        get_users()
        proslushka_poshla()
        connecting()

    

    def run(self):
        """Запускаем сервер"""
        try:
            main()
        except KeyboardInterrupt:
            close_server()






sock=Server()
sock.run()












