import socket

sock = socket.socket()
sock.bind(('', 9090))
log_set = open('file.log', 'a')
log_set.write("start working\n")
While True:

        sock.listen(1)
        log_set = open('file.log', 'a')
        log_set.write("server is waiting for connections...\n")
        conn, addr = sock.accept()
        log_set.write("User was conect\n")

        msg = ""

        break

msg += data.decode()
conn.send(data)

log_set.write("Recieved message from user\n")

conn.close()

