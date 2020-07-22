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

