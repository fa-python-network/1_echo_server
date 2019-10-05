import socket

try:
    portnum = int(input("Write port number\n"))

except:
    print("Wrong format of port number")

try:
    hostname = raw_input("Write hostname\n")

except:
    print("Wrong format of hostname")

sock = socket.socket()
sock.connect((hostname, portnum))

while True:

    msg = raw_input("Write <exit> to quit\n")

    if msg == "exit":
        sock.send(msg.encode())
        break

    sock.send(msg.encode())
    print("Message sent")

sock.close()


