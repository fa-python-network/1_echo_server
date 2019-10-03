import socket
port=int(input("Give me your port,client: "))
if not 0 <= port <= 65535:
    print('Wrong port from client')
sock=socket.socket()
sock.connect(('localhost',port))
msg=input("Enter your message: ")
while True:
    if msg != 'exit':
        sock.send(msg.encode())
        msg=input("Enter your message: ")
    else:
        print('Connection end')
        sock.close()
        break



    


