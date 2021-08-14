#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'
PORT = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('SERVER LISTENING ON PORT {0}...'.format(PORT))
s.listen(5)

while True:
    (conn, addr) = s.accept()
    print('Connected by', addr)
    while True:
        conn.send(b'Write a message: ')
        data = conn.recv(1024)
        if not data:
            break
        conn.send(b'We can repeat it! ')
        conn.sendall(data)