from socket import socket

sock = socket()
print('Launched')

host, port = '', 8000

sock.bind((host, port))
sock.listen(5)
print('Port sniffing')

while True:
    conn, addr = sock.accept()
    addr = addr[0]
    print(f'New client connected')

    data = b''
    while True:
        chunk = conn.recv(1024)
        data += chunk
        if len(chunk) < 1024:
            break

    text = data.decode()
    print(f'Sever have got "{text}" from {addr}')

    conn.send(data)
    print(f'{data} sent back to client')

    conn.close()
    print(f'Connection with {addr} finished')

sock.close()

print('Stopped')
