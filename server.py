import socket

sock = socket.socket()
sock.bind(('', 9090))
log_track = open('file.log', 'a')
log_track.write("Server started working\n")
while True:
    sock.listen(0)
    log_track = open('file.log', 'a')
    log_track.write("Server is waiting for connections...\n")
    conn, addr = sock.accept()
    log_track.write("User has been connected\n")

    msg = ''

    while True:
	    data = conn.recv(1024)
	    if not data:
		    break
	    msg += data.decode()
	    conn.send(data)
        
    log_track.write("Recieved message from user\n")
    log_track.write("Message has been sent to user\n")

    conn.close()
    log_track.write("User has been disconnected from the server\n")
    log_track.close()
