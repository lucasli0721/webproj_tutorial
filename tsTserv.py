#!/user/bin/env python

from socket import *
from time import ctime


def main():
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    try:
        while True:
            print('waiting for connection...')
            tcpCliSock, addr = tcpSerSock.accept()
            print(f'...connecting from: {addr}')

            while True:
                data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
                if not data:
                    break
                data = bytes(f'{ctime()} : {data}', 'utf-8')
                tcpCliSock.send(data)
            tcpCliSock.close()

    except KeyboardInterrupt or EOFError:
        tcpSerSock.close()


if __name__ == "__main__":
    main()
