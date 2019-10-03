import socket

sock = socket.socket()

host = input("Input host adress: " )
host1 = host.split('.')
for char in host1:
	if 0<=int(char)<=255:
		pass
	else:
		print("Incorrect IP")
		host = 'localhost'

port = int(input("Input host number: "))
if 1024<=port<=65535:
	pass
else:
	print("Incorrect port")
	port = 8080



sock.connect((host, port))
print(f'Client is connected to {port}')

while True:
	print('Input your message')
	data = input()
	if data == 'exit':
		break
	print('Message is sending')
	sock.send(data.encode())
	ans=sock.recv(1024) 
sock.close()
print("Server's answer is ")
print(ans.decode())
