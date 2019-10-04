import socket
import pickle
import os

port = 9090
clients = 1
client_file = 'clients.pkl'
clients_dict = {}

sock = socket.socket()
while True:

    try:
        sock.bind(('',port))
        break
            
    except:
        port += 1


sock.listen(clients)

if os.path.getsize(client_file) > 0:  #get client info
    with open (client_file, 'rb') as f:
        clients_dict = pickle.load(f)
    

while True:

    conn, addr = sock.accept()
    
    while True:
        
        if addr[0] in clients_dict.keys():
            msg = "Welcome " + clients_dict[addr[0]]
            conn.send(msg.encode())
        
        else:
            conn.send('Who_are_you'.encode()) # add new client
            data = conn.recv(1024)
            
            client_file.update({addr[0]:data.decode()})
            
            with open(client_file, 'wb') as f:
                pickle.dump(client_file, f)
            

        break
        
    conn.close()
    print("Connection is cut off")

