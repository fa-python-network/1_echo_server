import socket

def host_port(sock, host = 'localhost', port = 9090):
    if 0>port>65535:
        print("Неправильный номер порта")
        port=int(input("Введите другой номер"))
        host_port(host, port, sock)
    else:
        sock.connect(('localhost', 9090))
    

sock = socket.socket()

sock.send(b'helloo, world!')

while True:
    data = sock.recv(1024)
    flag=input("Введите exit для остановки, нажмите enter для продолжения")
    if flag == "exit":
        break
    
sock.close()

print (data)