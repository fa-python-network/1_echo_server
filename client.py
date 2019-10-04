import socket
import hashlib
import re
from os import listdir


def settings():
    host_prompt = input('Type the HOST if needed: ')
    port_prompt = input('Type the PORT if needed: ')

    global HOST
    global PORT
    HOST = '127.0.0.1' if not host_prompt else host_prompt
    PORT = 9014 if not port_prompt else int(port_prompt)


def modify_password(password: str) -> str:
    hash_object = hashlib.md5(password.encode())
    return hash_object.hexdigest()


def create_cookie(cookie: str) -> None:
    with open('cookie', 'w') as f:
        f.write(cookie)


if __name__ == '__main__':
    settings()

    with socket.socket() as s:
        s.connect((HOST, PORT))

        if 'cookie' in listdir():
            with open('cookie', 'r') as f:
                s.sendall(f.readline().encode())

        while True:
            data = s.recv(1024)
            print(data.decode())

            reply = input()

            if re.match(r'(\w+);(\w+)', reply):
                re_reply = re.search(r'(\w+);(\w+)', reply)
                user_name, password = re_reply.group(1), modify_password(re_reply.group(2))
                reply = f'{user_name};{password}'
                create_cookie(modify_password(re_reply.group(2)))
            
            s.sendall(bytes(reply, 'utf-8'))
