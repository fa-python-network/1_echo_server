import socket

sock = socket.socket()
print("Connection to server")
sock.connect(('localhost', 9090))
while True:
    msg = input("Введите сообщение для сервера: ")
    print("Sending data to server")
    sock.send(msg.encode())
    if msg == "exit":
        break


print("Taking data from server")
data = sock.recv(1024)

print("Disconnected with server")
sock.close()

print(data.decode())
