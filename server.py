import socket
import re
import time
import json

lgf = open("logfile.txt", "a+")


def user_management(new_host):
    try:
        users_source = open("users_list.json", "r")
        usrs = users_source.read()
        users_current = json.loads(usrs)
        users_source.close()

    except:
        users_current = dict()

    if new_host in list(users_current.keys()):
        conn.send(("hi, "+users_current[new_host]+"\n").encode())

    else:
        conn.send(("WELCOME TO THE SYSTEM, REGISTERING "+new_host+"\n").encode())
        conn.send("Vvedite imya, pod\nkotorym vas zapomnit sistema:\n".encode())
        name = conn.recv(1024).decode()
        conn.send(("REGISTERED USER" + ' "' + name + '" ' + "SUCCESSFULLY\n").encode())
        users_current.update({new_host: name})

    users_out = open("users_list.json", "w+")
    json.dump(users_current, users_out)
    users_out.close()


def checker():
    port = "4000"
    host = "localhost"
    print("default host is 127.0.0.1(localhost)\n"
          "default port is 4000"
          )
    while True:
        uhost = input("vvedite host:\n")
        if uhost == "default" or uhost == "localhost" or uhost == "lh":
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
    resu = [host, int(port)]
    return resu


res = checker()
sock = socket.socket()
while True:
    try:
        print("\nTRYING PORT =", res[1], "\n")
        sock.bind((res[0], res[1]))
        break
    except:
        print("PORT ALREADY IN USE, TRYING THE NEXT ONE\n")
        res[1] += 1

sock.listen(0)
msg = ""
print("SERVER IS ON PORT", res[1])
# lgf.write(time.ctime()+"\nSERVER UP AND RUNNING\nLIST OF CONNECTIONS:\n\n")
print(time.ctime()+"\nSERVER UP AND RUNNING\nLIST OF CONNECTIONS:\n\n")
while True:
    conn, addr = sock.accept()
    # lgf.write(time.ctime() + f"\nCONNECTION FROM IP = {addr[0]} PORT = {addr[1]}\nMESSAGES:\n\n")
    print(time.ctime() + f"\nCONNECTION FROM IP = {addr[0]} PORT = {addr[1]}\nMESSAGES:\n\n")
    user_management(addr[0])
    while True:
        try:
            data = conn.recv(1024)
        except:
            print(time.ctime() + "\nCLIENT DISCONNECTED\n\n")
            # lgf.write(time.ctime() + "\nCLIENT DISCONNECTED\n\n")
            break
        if not data:
            print(time.ctime() + "\nCLIENT DISCONNECTED\n\n")
            # lgf.write(time.ctime() + "\nCLIENT DISCONNECTED\n\n")
            break
        msg += data.decode()
        # conn.send(data)
        # lgf.write(data.decode()+"\n\n")
        print(data.decode()+"\n\n")

conn.close()
lgf.close()
