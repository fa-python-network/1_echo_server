import socket
while True:
	print("Choose port between 1024 and 65535")
	port=int(input())
	if 65535>=port>=1024:
		break
	print("Mistakes were made....")

sock = socket.socket()
while True:
	try:
		sock.bind(('', port))
	except: 
		port=port+1
	else:
		break
print("Port is ",port)


log = open('log.txt','w')
log.write("Server starts working!")
sock.listen(0)
msg=''
for i in range(3):

	conn, addr = sock.accept()
	print(addr[0])

	msg = ''
	names = open('names.txt','r')
	nameflag=0
	for i in names:
		
		if i.split(',')[0]=="['"+addr[0]+"'":
			conn.send(str("Hello, "+str(i.split(',')[1])[2:-3]).encode())
			nameflag=1
			break

	names.close()
	if nameflag==0:
		conn.send(("Enter your name please").encode())
		name=(conn.recv(1024)).decode()
		names = open('names.txt','a')
		names.write(str([addr[0],name])+"\n")
		names.close()
		
 


	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)
	log.write("Message is received")
	print(msg)
	conn.close()
log.close()
