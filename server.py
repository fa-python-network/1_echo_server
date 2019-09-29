import socket
sock = socket.socket()
sock.bind(("",9094))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    print(addr)
    msg =''
    data = conn.recv(1024)
    print(f'Data: {data.decode()}')
    msg = data.decode()    
    print(f'MSG: {msg}')
    conn.send(msg.encode())
    conn.close()
