#!/usr/bin/env python

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print(f'...connecting from: {self.client_address}')
        data = (f"{ctime()}:{self.rfile.readline().decode('utf-8')}").encode('utf-8')
        self.wfile.write(data)

def main():
    tcpServ = TCP(ADDR, MyRequestHandler)
    print('waiting for connection...')
    tcpServ.serve_forever()


if __name__ == "__main__":
    main()
