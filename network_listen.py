#!/usr/bin/python

import socket
from threading import Thread
rom SocketServer import ThreadingMixInf


class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print "[+] New thread started for " + ip + ":" + str(port)

    def run(self):
        while True:
            data = conn.recv(2048)
            if not data: break
            print "received data:", data
            conn.send(data)  # echo


TCP_IP = '0.0.0.0'  # <-- Change this to the ip you to listen on.
TCP_PORT = 12345    # <-- Change this to a non-well known port > 1024
BUFFER_SIZE = 20    # <-- The smaller the buffer the quicker it'll send.  Client should mirror this for best results.


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(4)
    print "Waiting for incomin"
    (conn, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()