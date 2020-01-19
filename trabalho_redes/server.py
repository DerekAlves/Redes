#!/usr/bin/python

import socket
import threading
import os
import random
import linecache
import time



def print_word(word):
	for letter in word:
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

shift = 0
index = 0
life_counter = 6
#manages each thread received
def thread_management(server_input, word, or_word, list_server_input):
	global life_counter
	global shift
	global index
	global prints
	flag = True
	textRecv = "Recebido!"
	textGO = "GAME OVER"
	textYW = "YOU WIN!"
	while flag:
		life_str =  str(life_counter)
		server_input.sendall(life_str.encode('utf-8'))
		response = server_input.recv(1024)
		response = response.rstrip()
		if list_server_input[shift] == server_input and response.decode() != 'sair':
			print("Mensagem do cliente:", response.decode())	
			if response.decode() in or_word and response.decode() not in word:
				for i in range(0, len(or_word)):
					if response.decode() is or_word[i]:
						word[i] = or_word[i]	
			else:
				life_counter = life_counter - 1
				print(life_counter)		
			if life_counter == 0:
				print('GAME OVER')
				print_hangman(life_counter)
				server_input.sendall(textGO.encode('utf-8'))
				flag = False
				break	
			if '_' not in word:
				print('YOU WIN!')
				print_word(word)
				server_input.sendall(textYW.encode('utf-8'))
				flag = False
				break		
			shift = (shift+1)%index
			print_hangman(life_counter)		
			print_word(word)				
		elif response.decode() == 'sair':
			print('saiu alguém')
			list_server_input.remove(server_input)
			index = index-1	
			flag = False
			break	
		#if index == shift:
	time.sleep(.015)
	life_str = str(life_counter)
	server_input.sendall(life_str.encode('utf-8'))
	server_input.close()		#break	

#########################################################			

path = './palavras/'
files = os.listdir(path)
i = random.choice((0,len(files)-1))
file_name = path + files[i]
f = open(file_name, 'r')
line_number = random.choice((1,sum(1 for line in f)))
word = linecache.getline(file_name, line_number)[0:-1]
print('Dica:', files[i][0:-4])

w = []
for i in range(0, len(word)):
	w.append('_')	
print_word(w)	

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
server_socket.bind(address)
server_socket.listen(15)

# Print
list_server_input = []
while True:
	server_input, address = server_socket.accept()
	if index < 5:
		list_server_input.append(server_input)
		print("Nova conexao recebida de ", address)
		thread = threading.Thread(target = thread_management, args = (server_input, w, word, list_server_input))
		thread.start()
		index = index+1




#if list_server_input[shift] == server_input: