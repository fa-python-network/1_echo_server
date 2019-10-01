import socket
import re


def checker():
    port = "4000"
    host = "localhost"
    print("default host is 127.0.0.1(localhost)\n"
          "default port is 4000"
          )
    while True:
        uhost = input("vvedite host:\n")
        if uhost == "default" or uhost == "localhost":
            break
        elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', uhost) == None:
            print("try again")
        else:
            host = uhost
            break
    while True:
        uport = input("vvedite port:\n")
        if uport == "default" or uport == "4000":
            break
        elif not uport.isnumeric() == True or int(uport)<1024 or int(uport) > 65535:
            print("try again")
        else:
            port = uport
            break
    return host, int(port)


res = checker()         
sock = socket.socket()
sock.bind(res)
sock.listen(0)
msg = ""
print("\nSERVER UP AND RUNNING\nLIST OF CONNECTIONS:\n")
while True:
	conn, addr = sock.accept()
	print(f"CONNECTION FROM\nIP = {addr[0]} PORT = {addr[1]} \n")
	while True:
		data = conn.recv(1024)
		if not data:
			print("CLIENT DISCONNECTED\n")
			break
		msg += data.decode()
		# conn.send(data)
		print(data.decode(),'\n')


conn.close()
