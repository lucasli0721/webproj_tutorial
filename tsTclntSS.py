#!/user/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def main():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = input('> ')
        if not data:
            break
        data = (f'{data}\r\n').encode('utf-8')
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        if not data:
            break
        print(data.strip())
        tcpCliSock.close()


if __name__ == "__main__":
    main()
