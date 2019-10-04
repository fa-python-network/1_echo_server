import socket
import re


port = input("Enter the port")
host = input("Enter the host")

try:
    
    if (int(port) > 1024) and (int(port) < 65000:
        port = int(port)
    else:
        port = 9090
            
except:
    port = 9090

try:

    check_host = re.search('^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$', port, flags=re.IGNORECASE)
    
    if (host != 'localhost') and (checkhost is None):
        host = 'localhost'
        
except:
    host = 'localhost'
        
    

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


