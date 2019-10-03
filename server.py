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
log.write("Server starts working!\n")
sock.listen(0)
msg=''
for j in range(3):
	check=False
	conn, addr = sock.accept()
	print(addr[0])

	names = open('names.txt','r')
	nameflag=0
	for i in names:
		
		if i.split(',')[0]=="['"+addr[0]+"'":
			
			nameflag=1
			
			message=str((i.split(',')[1])[2:-3]).encode()
			conn.send(message)
			password=(conn.recv(1024)).decode()

			
			if i.split(',')[2][2:-3]==password:
					
					print("\nPassword is right")
					check=True
					break
			if check==False:
				print('\nPassword is wrong!')

	names.close()
	if nameflag==0:
		
		conn.send(("NamePassword").encode())
		namepass=(conn.recv(1024)).decode()
		name=namepass.split(',')[0]
		password=namepass.split(',')[1]
		names = open('names.txt','a')
		names.write(str([addr[0],name,password])+"\n")
		names.close()
		check=True
	
	msg = ''
	while check:
		
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)
	log.write("Message is received\n")
	print(msg)
conn.close()
log.close()
