import socket

with open('log.txt', 'a') as f:
    pass

sock = socket.socket()

port = 1024

while port != 65536:
	try:
		sock.bind(('', port))
		break
	except:
		port+=1

print("Your port is: \n", port)

sock.listen(1)

while True:
    
    conn, addr = sock.accept()
    with open('log.txt', 'a') as f:
        f.write(str(addr[0])+'\n')

    msg = ''
    data = conn.recv(1024)
    msg = data.decode()
    with open('log.txt', 'a') as f:
        f.write(msg+ '\n')
    if not data:
        break

with open('log.txt', 'a') as f:
    f.write('\n')

conn.send(data)
print (msg)