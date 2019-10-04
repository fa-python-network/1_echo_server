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

service_file = open("serviceCommand.log", "a")

sock = socket.socket()
sock.bind(('', port))
sock.listen(clients)

while True:

    conn, addr = sock.accept()
    
    while True:
        
        service_file.close()
        service_file.open("serviceCommand.log", "a")
        
        data = conn.recv(1024)
        if not data:
            break
            
      	conn.send(data)
        service_file.Write("Answer sent")
        
    conn.close()
    service_file.Write("Connection is cut off")
    service_file.close()
