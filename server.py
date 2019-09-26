import socket
while True:
    sock=socket.socket()
    port=int(input())
    if not 0 <= port <= 65535:
        with open('dannye.txt','w') as f:
            f.write('Wrong port from server')
    else:
        port=9090
    sock.bind(('',9090))
    sock.listen(1)
    conn,addr=sock.accept()
    #msg=''
    while True:
        dan=conn.recv(1024)
        if dan:
            with open('dannye.txt','w') as f:
                f.write(dan.decode())
        else:
            conn.close()
        break
#print(msg)
conn.close()

   


