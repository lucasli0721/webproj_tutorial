#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print(f'...connecting from {clnt}')

    def dataReceived(self, data):
        data = data.decode('utf-8')
        data = (f'{ctime()} : {data}').encode('utf-8')
        self.transport.write(data)


def main():
    factory = protocol.Factory()
    factory.protocol = TSServerProtocol
    print('waiting for connection...')
    reactor.listenTCP(PORT, factory)
    reactor.run()


if __name__ == "__main__":
    main()
