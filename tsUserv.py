#!/user/bin/env python

from socket import *
from time import ctime


def main():
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)

    try:
        while True:
            print('waiting for message...')
            data, addr = udpSerSock.recvfrom(BUFSIZ)
            data = bytes(f"{ctime()} : {data.decode('utf-8')}", 'utf-8')
            udpSerSock.sendto(data, addr)
            print(f'receive from and return to {addr}')
    except KeyboardInterrupt or EOFError:
        udpSerSock.close()


if __name__ == "__main__":
    main()
