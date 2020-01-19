#!/usr/bin/python

import socket

def print_word(word):
  for letter in word:
    if letter != "'" and letter != ',' and letter != '[' and letter != ']' and letter != ' ':
      print(letter, end = " ")
  print('\n')   

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
hint = client_socket.recv(1024)
hint = hint.rstrip()
hint = hint.decode()
print('Dica:', hint)

while flag:

    response = client_socket.recv(1024)
    response = response.rstrip()
    life = int(response.decode())
    print_hangman(life)

    response = client_socket.recv(1024)
    response = response.rstrip()
    state = response.decode()
    print_word(state)

    
    response = client_socket.recv(1024)
    response = response.rstrip()
    response = response.decode()
    print(response)


    if response == 'Fim de jogo' or response == 'Vocês ganharam!':
        flag = False
    elif 'Seu turno' in response:
        text = input("Informe texto ou digite 'sair' para desconectar: " )
        if text == 'sair':
            flag = False
        client_socket.sendall(text.encode('utf-8'))


response = client_socket.recv(1024)
response = response.rstrip()
life = int(response.decode())
print_hangman(life)            
print("Conexão encerrada!")
client_socket.close()