#!/usr/bin/python

import socket

def print_hangman(life_counter):
    
    prints =   [" _____________\n|      |      |\n|             |\n|             |\n|             |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|             |\n|             |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|      |      |\n|             |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|     /|      |\n|             |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|     /|\\     |\n|             |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|     /|\\     |\n|     /       |\n|             |\n|_____________|\n"
               ," _____________\n|      |      |\n|      O      |\n|     /|\\     |\n|     / \\     |\n|             |\n|_____________|\n"]

    print(prints[6 - life_counter], "\n")

address = ("localhost", 20000)

# Create sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

# Echo
flag = True
while flag:
    response = client_socket.recv(1024)
    response = response.rstrip()
    print(response.decode())
    if response.decode() == 'GAME OVER' or response.decode() == 'YOU WIN!':
        flag = False
    else:
        life = ord(response.decode())
        print_hangman(life-48)
        text = input("Informe texto ou digite 'sair' para desconectar: " )
        client_socket.sendall(text.encode('utf-8'))
        #print(response)
        if (text == "sair"):
            flag = False
            #break

response = client_socket.recv(1024)
response = response.rstrip()
life = ord(response.decode())
print_hangman(life-48)            
print("Conexão encerrada!")
client_socket.close()