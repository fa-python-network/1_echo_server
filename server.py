import socket

f = open ('log.txt', 'w')
sock = socket.socket()
port = 9090
while True:
	try:
		if (port == 65536):
			print('Все порты заняты')
			break
		sock.bind(('', port))
		break
	except:
		port += 1
print(f'Port number: {port}')
print("Server starts", file = f)
sock.listen(0)
print("Now listen", file = f)
conn, addr = sock.accept()

msg = ''

while True:
	data = conn.recv(1024)
	print("new data from client", file = f)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
	print("data to client", file = f)

print(msg)

conn.close()
print('stop client', file = f)
f.close