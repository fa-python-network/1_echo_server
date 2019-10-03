import socket
import random
sock=socket.socket()
port=int(input("Give me your port, server: "))
if not 0 <= port <= 65535:
    print('Wrong port from server')
else:
    try:
        sock.bind(("",port))
    except Exception:
        while True:
            port=random.randint(0,65535)
            try:
                sock.bind(("",port))
                print("Listening port:", port)
            except:
                pass
            else:
                break
    else:
        print("Listening port",port)
sock.listen(1)
f=open('forIP.txt','tw')
f.close()
f=open('forIP.txt','r')
while True:
    conn,addr=sock.accept()
    if str(addr[0]) in f.read() :
        print('Hello IP',addr[0])
    else:
        f.close()
        f=open('forIP.txt','a')
        f.write(str(addr[0]))
        f.close() 
    while True:
        dan=conn.recv(1024)
        if dan:
            print(dan.decode())
        else:
            conn.close()
        break
    conn.close()

   


