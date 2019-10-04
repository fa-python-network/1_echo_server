import socket

port = "9090"
host = "localhost"

sock = socket.socket()
sock.connect((host, port))

while True:
    print("Enter the message")
    msg = input()
    
    if msg == 'exit': #прекращаем работу с сервером 
        break
    
    print("Messagge sent")
    sock.send(msg.encode())
    
    print("answer")
    data = sock.recv(1024) 
    
    print(data.decode())

print("Connection is cut off")
sock.close()


