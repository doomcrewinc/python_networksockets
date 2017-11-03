#!/usr/bin/python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 64
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

TCP_IP = '0.0.0.0'  # <-- Change this to the ip you want to connect to (SERVER)
TCP_PORT = 12345    # <-- Change this to a non-well known port > 1024 (MUST MIRROR SERVER)
BUFFER_SIZE = 20    # <-- The smaller the buffer the quicker it'll send.  It's a good idea to keep the buffer size consistant on both the client and server to prevent TCP/IP resends.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    # conn.send(data)  # echo
    if "/version" in data:
        conn.send("PoC - Client - 0.0.1")

    if "/echo" in data:
        data = data.replace("/echo", "")
        conn.send(data + "n")

conn.close()