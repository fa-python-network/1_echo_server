def sendmsg(who, msg):
    msg_len = str(len(msg))
    while len(msg_len) < 5:
        msg_len = '0' + msg_len
    who.send((msg_len + msg).encode())


def checkmsg(who):
    msg_len = int(who.recv(4).decode())
    msg = who.recv(msg_len).decode()
    return msg