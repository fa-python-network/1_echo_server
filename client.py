import socket
from time import sleep

SERVER_IP = "127.0.0.1"
PORT_NUMBER = 9090

class Client:
    def __init__(self) -> None:
        sock = socket.socket()
        sock.setblocking(1)
        sock.connect((SERVER_IP, PORT_NUMBER))
        self.sock = sock
        #Работа с данными, поступающими от пользователя
        self.user_processing()
        #Закрываем сокет
        self.sock.close()
        
    def user_processing(self):

        while True:
            msg = input("-> ")
            #Если сообщение exit
            if msg == "exit": break
            #Если ничего не ввели
            if msg == "": msg = "None"
        
            #Отправляем сообщение
            self.sock.send(msg.encode())
            #Получаем ответ
            data = self.sock.recv(1024)

            print(f"Ответ от сервера: {data.decode()}")

def main():
    client = Client()

if __name__ == "__main__":
	main()