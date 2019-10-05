import socket, csv

sock = socket.socket()
                                                       
num_sock = int(input("Enter the socket number: "))

try:                                               
	sock.bind(('localhost', num_sock))
except socket.error:
		print("This Adress already in use. This is free one: ")
		for i in range(1024,65536):
			try:
				sock.bind(('', i))
				f = i
				break
			except socket.error:
				pass
try:
	print (f)
except NameError:
	pass
sock.listen(3)

while True:

	conn, addr = sock.accept()
	af = 0
	start = 2
	with open ("log.txt", 'a') as f:
		f.write(str(addr))
		f.write('\n')
		f.close()
	
	with open ("users.csv", 'r') as f:
		csv_reader = csv.reader(f)
		for line in csv_reader:
			if line[0] == addr[0]:
				conn.send("Hello, "+line[1] + ' ')
				af = 1
				start = 1
		f.close()

	if af == 0:
		with open ("users.csv", 'a') as f:
			writer = csv.writer(f)
			username = ''
			conn.send("Hello! Please, enter your name: ")
			while True:
				data = conn.recv(1024)
				if not data:
					break
				username += data.decode()
			writer.writerow([addr[0],username])
			f.close()
	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data.decode().upper().encode())
	
conn.close()
print(msg)