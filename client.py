import socket
port=int(input("Give me your port,client: "))
if not 0 <= port <= 65535:
    with open('dannye.txt','w') as f:
        f.write('Wrong port from client')
else:
    port=9092
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
#sock.close()


    


