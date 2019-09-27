import socket
sock=socket.socket()
port=int(input("Give me your port, server: "))
if not 0 <= port <= 65535:
    with open('dannye.txt','w') as f:
        f.write('Wrong port from server')
else:
    port=9092
sock.bind(('',9092))
sock.listen(1)
while True:
    conn,addr=sock.accept()
    while True:
        dan=conn.recv(1024)
        if dan:
            with open('dannye.txt','w') as f:
                f.write(dan.decode())
        else:
            conn.close()
        break
    conn.close()

   


