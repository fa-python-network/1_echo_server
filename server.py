import socket

port = input()
clients = 1

try:
    
    if (int(port) > 1024) and (int(port) < 65000:
        port = int(port)
    else:
        port = 9090
            
except:
    port = 9090

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(clients)

while True:

    conn, addr = sock.accept()
    
    while True:
        
        data = conn.recv(1024)
        if not data:
            break
            
      	conn.send(data)
        print("Answer sent")
        
        conn.close()
        print("Connection is cut off")
