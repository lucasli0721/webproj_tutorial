#!/usr/bin/env python

from twisted.internet import protocol, reactor


HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print(f'...sending {data}...')
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    ClientConnectionLost = ClientConnectionFailed = lambda self, connector, reason: reactor.stop()


def main():
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()


if __name__ == "__main__":
    main()
