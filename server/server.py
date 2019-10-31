import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)

print(msg)

conn.close()
import socket, errno
import sys

class Server(socket.socket):

    def __init__(self):
        super().__init__()
        self.sock=socket.socket()


    def send_msg(self, msg, sock):
        length_msg = str(len(msg))
        length_msg = '0'*(10-len(length_msg)) + length_msg
        msg = length_msg + msg
        sock.send(msg.encode())

    def recv_msg(self, sock):
        try:
            length_msg = int(sock.recv(10).decode())
        except ValueError:
            msg = None
        else:
            msg = sock.recv(length_msg).decode()
        return msg


    def close_server(self):
        with open ('log.txt', 'a') as file:
            print('Остановка сервера', file=file)
        self.sock.close()
        sys.exit()

    def new_user(self, conn, addr, d):
        name = self.recv_msg(conn)
        password = self.recv_msg(conn)
        d[addr[0]] = d.get(addr[0], [name, password])
        with open ('users.txt', 'w') as users:
            print(d, file=users)


    def old_user(self, conn, addr, d):
        passwd = d[addr[0]][1]
        password = self.recv_msg(conn)
        if passwd == password:
            self.send_msg('0', conn)
            self.recv_msg(conn)
            return
        else:
            self.send_msg('1', conn)
            self.old_user(conn, addr, d)



    def sha_podklyuchimsya(self):
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
        try:
            with open ('users.txt', 'r') as users:
                self.d = eval(users.read())
        except FileNotFoundError:
            with open ('users.txt', 'w') as users:
                self.d={}
        except SyntaxError:    
                self.d={}


    def proslushka_poshla(self):
        self.sock.listen(1)

        with open ('log.txt', 'a') as file:
	        print('Начало прослушивания порта', file=file)



    def connecting(self):
        while True:

            conn, addr = self.sock.accept()
            with open ('log.txt', 'a') as file:
                print('Подключение клиента', file=file)		

            if addr[0] not in self.d.keys():
                flag = str(1)
                self.send_msg(flag, conn)
                self.new_user(conn, addr, self.d)
            else:
                flag = str(0)
                self.send_msg(flag, conn)
                self.old_user(conn, addr, self.d) 

            msg = 'Hello ' + self.d[addr[0]][0]
            self.send_msg(msg, conn)

            self.chatting(conn)

    def chatting(self, conn):            
        while True:
                data = self.recv_msg(conn)
                with open ('log.txt', 'a') as file:
                    print('Приём данных от клиента', file=file)
                if not data:
                    conn.close()
                    break

                self.send_msg(data.upper(), conn)
                with open ('log.txt', 'a') as file:
                    print('Отправка данных клиенту', file=file)


        with open ('log.txt', 'a') as file:
                print('Отключение клиента', file=file)



    def work(self):
        self.sha_podklyuchimsya()
        self.get_users()
        self.proslushka_poshla()
        self.connecting()



    def run(self):
        try:
            self.work()
        except KeyboardInterrupt:
            self.close_server()

sock=Server()
sock.run()
