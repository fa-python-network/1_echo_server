import socket
import threading
import time

tLock = threading.Lock()
shutdown = False
join = False

def receving (name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()


host = "127.0.0.1"
port = 0

server = (host,5000)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

alies = raw_input("Your name: ")
message = raw_input(alies + " send to")
while  message != 'q':
    if message != '':
        s.sendto(alies + ": " + message, server)
    tLock.acquire()
    message = raw_input(alies + " send to")
    tLock.release()
    time.sleep(0.2)

shutdown = True
rT.join()
s.close()