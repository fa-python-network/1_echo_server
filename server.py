import socket

port = 9090
clients = 1

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
