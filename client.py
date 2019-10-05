import socket

while True:

    try:
        portnum = int(input("Write port number\n"))
        if 1024 <= portnum <= 65535:
            break
        else:
            print("Wrong format of port number")

    except:
        print("Wrong format of port number")

while True:

    try:
        hostname = raw_input("Write host address\n")
        for i in hostname.split("."):
            if 255 < int(i) or int(i) < 0:
                print("Wrong format of hostname")
                break
        break

    except:
        print("Wrong format of hostname, set default")
        hostname = "localhost"
        break

sock = socket.socket()
sock.connect((hostname, portnum))

while True:

    data = sock.recv(1024)
    print(data.decode())

    if data.decode() == "Who are you?":
        name = raw_input()
        sock.send(name.encode())

    if "Welcome" in data.decode():
        break

while True:

    msg = raw_input("Write <exit> to quit\n")

    if msg == "exit":
        sock.send(msg.encode())
        break

    sock.send(msg.encode())
    print("Message sent")

sock.close()


