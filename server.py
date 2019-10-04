import socket

port = 9090
clients = 1

try:
    
    sock.bind(('',port))
    break
            
except:
    port += 1

service_file = open("serviceCommand.log", "a")

service_file.Write(f'Port № {port} has been installed')

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
