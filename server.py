from socket import socket


def main():
    while True:
        conn, addr = sock.accept()
        addr = addr[0]
        print(f'Connected to "{addr}"')

        data = ''
        while True:
            chunk = conn.recv(1024).decode()
            data += chunk
            if len(chunk) < 1024:
                break

        print(f'Sever received "{data}" from {addr}')

        conn.send(data.encode())
        print(f'{data.encode()} sent back to client')

        conn.close()
        print(f'{addr} disconnected')
    

with socket() as sock:
    print('Server started here')

    sock.bind(('', 8888))
    sock.listen(8)
    print('Port listening started')

    main()

print('"main" finished')
