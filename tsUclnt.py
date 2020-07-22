#!/user/bin/env python

from socket import *


def main():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    udpCliSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input('> ').encode('utf-8')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    udpCliSock.close()


if __name__ == "__main__":
    main()
