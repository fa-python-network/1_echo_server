import socket
from time import sleep

SERVER_IP = "127.0.0.1"
PORT_NUMBER = 9090

def main():
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect((SERVER_IP, PORT_NUMBER))


    #2. Модифицируйте код клиента таким образом, чтобы он читал строки в цикле до тех пор, пока клиент не введет “exit”.
    while True:

        msg = input("-> ")
        #Если сообщение exit
        if msg == "exit":
            break

        #Отправляем сообщение
        sock.send(msg.encode())
        #Получаем ответ
        data = sock.recv(1024)

        print(f"Ответ от сервера: {data.decode()}")

    sock.close()
if __name__ == "__main__":
	main()