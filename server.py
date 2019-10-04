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
	nameflag=0#user is unknown

	for i in names:#check ip in names.txt
		
		if i.split(',')[0]=="['"+addr[0]+"'":#if ip is known
			
			nameflag=1#user is known
			
			message=str((i.split(',')[1])[2:-1]+'!').encode()#send username!
			
			conn.send(message)
			password_msg='1'
			password_txt=""
			while password_msg[-1]!='!':
				password_msg=(conn.recv(1024)).decode()
				password_txt+=password_msg

			
			if i.split(',')[2][2:-3]==password_txt[:-1]:
			#If password is right		
					print("\nPassword is right")
					check=True
					break
			if check==False:
				print('\nPassword is wrong!')

	names.close()
	if nameflag==0:
		
		conn.send(("NamePassword!").encode())
		namepass_msg='1'
		namepass_txt=''
		while namepass_msg[-1]!='!':
			namepass_msg=(conn.recv(1024)).decode()
			namepass_txt=namepass_txt+namepass_msg
		name=namepass_txt.split(',')[0]
		password=namepass_txt.split(',')[1][:-1]
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
