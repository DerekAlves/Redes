#!/usr/bin/python

import socket

address = ("localhost", 20000)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

# Echo
while True:
    text = input("Informe texto ou digite 'sair' para desconectar: " )
    client_socket.sendall(text.encode('utf-8'))
    if (text == "sair"):
        client_socket.close()
        break
