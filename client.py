import socket


def main():
    sock.connect(('localhost', num_port))
    answer = sock.recv(1024)
    if answer.decode() == "OK":
        answer = sock.recv(1024)
        print(answer.decode())
        client_password_check = input()
        sock.send(client_password_check.encode())
        answer = sock.recv(1024)
        if answer.decode() == "OK":
            print("Вы успешно авторизованы")
        if answer.decode() == "FAIL":
            print("Вы ввели неверный пароль")
            sock.send("exit".encode())
            return
    else:
        client_name = input("Input your name: ")
        if not client_name:
            client_name = "Client"
        client_password = input("Придумайте пароль: ")
        sock.send(client_name.encode())
        sock.send(client_password.encode())
    while True:
        msg = input("Input a message to server: ")
        print("Sending data to server")
        sock.send(msg.encode())
        if msg == "exit":
            return

sock = socket.socket()
num_port = input("Input port number of server: ")
try:
    num_port = int(num_port)
except:
    num_port = 4412
    print("incorrect format of port number")
print("Connection to server")
main()
print("Taking data from server")
data = sock.recv(1024)
print("Disconnected with server")
sock.close()
print(data.decode())
