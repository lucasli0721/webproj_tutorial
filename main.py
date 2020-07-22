import socket
"""
TODO: pseudo code for setting tcp server
ss = socket.socket()
ss.bind()
ss.listen()
inf_loop:
    cs = ss.accept()
    comm_loop:
        cs.recv()/cs.send()
    cs.close()
ss.close()
"""

"""
TODO: pseudo code for setting tcp client
cs = socket.socket()
cs.connect()
comm_loop:
    cs.send()/cs.recv()
cs.close()
"""

"""
TODO: pseudo code for setting ucp server
ss = socket.socket()
ss.bind()
inf_loop:
    ss.recvfrom/ss.sendto()
ss.close()
"""

"""
TODO: pseudo code for setting ucp client
cs = socket.socket()
comm_loop:
    cs.recvfrom/ss.sendto()
cs.close()
"""
