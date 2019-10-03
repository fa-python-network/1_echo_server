import socket
class Myserver(socket.socket):
    def newmessage(self):
        length = self.recv(1020).decode()
        if length != '':
            message = self.recv(int(length)).decode()
            return message


    def sendmessage(self, message):
        length0 = str(len(message))
        self.send(length0.encode())
        self.send(message.encode())

    def newclient(self):
        fd, addr = self._accept()
        sock = Myserver(self.family, self.type, self.proto, fileno=fd)
        return sock, addr


