import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
PORT = input("Enter port to connect: ")
HOST = input("Enter host to connect: ")
if PORT == '':
    PORT = 9090
if HOST == '':
    HOST = 'localhost'
sock.connect((HOST, PORT))
while True:
    data = ""
    msg = input("Enter your message to server or 'exit' to quit: ")
    if msg.lower() == "exit":
        break
    sock.send(msg.encode())
    print("This was sent to ", HOST, ":", msg)

data = sock.recv(1024)
print("This was recieved from server: ")
print(data.decode())

sock.close()
print("Connection with", HOST, "was closed")

