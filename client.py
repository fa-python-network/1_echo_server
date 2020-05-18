import socket
import logging

logging.basicConfig(filename="client.log", level=logging.INFO)


def set_host():
    while True:
        print('Type HOST below or write "def" for default HOST')
        try:
            msg = input()
            if msg == "def":
                host = '127.0.0.1'
            else:
                host = msg
            break
        except:
            log = 'You enter not supported HOST, please try again'
            logging.error(log)
            print(log)
    return host


def set_port():
    while True:
        print('Type PORT below or write "def" for default PORT')
        try:
            msg = input()
            if msg == "def":
                port = 9090
                break
            elif msg is not int:
                print('You enter not supported PORT, please try again')
            else:
                port = msg
                break
        except:
            log = 'You enter not supported PORT, please try again'
            logging.error(log)
            print(log)
    return port

def set_login():
    while True:
        print('Type your login')
        try:
            msg = input()
            if type(msg) is not str:
                print("not str")
                print('You enter not supported login, please try again')
            else:
                login = msg
                break
        except:
            log = 'You enter not supported login, please try again'
            logging.error(log)
            print(log)
    return login


def set_passwd():
    while True:
        print('Type your password')
        try:
            msg = input()
            if type(msg) is not str:
                print('You enter not supported password, please try again')
            else:
                passwd = msg
                break
        except:
            log = 'You enter not supported login, please try again'
            logging.error(log)
            print(log)
    return passwd


LOGIN = set_login()
PASSWD = set_passwd()
HOST = set_host()
PORT = set_port()

sock = socket.socket()
try:
    sock.connect((HOST, PORT))
    data = ''
    print('Write your message below:')

    while True:
        msg = input()
        if msg == 'exit':
            break
        data += msg
        log = "Current message: %s\n You can continue write messages, or write 'exit' for sending message" % data
        logging.info(log)
        print(log)

    try:
        data = "%s:%s:%s" % (LOGIN, PASSWD, data)
        sock.send(data.encode())
        log = 'Your message was sent successfully'
        logging.info(log)
        print(log)
    except Exception as ex:
        logging.error(ex)
        print(ex)

    try:
        msg = sock.recv(1024).decode()
        log = '\nYou have receive new message: \n%s' % msg
        logging.info(log)
        print(log)
    except Exception as ex:
        logging.error(ex)
        print(ex)

    sock.close()

except Exception as ex:
    log = "Failed to connect to server\nException is: %s" % ex
    logging.error(log)
    print(log)
