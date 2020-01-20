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

local = '0.0.0.0'

address = (local, 20000)
shift = 0
index = 0
life_counter = 6
end = False
list_server_input = []
#manages each thread received
def thread_management(server_input, word, or_word, tip):
	global life_counter
	global shift
	global index
	global prints
	global end
	global list_server_input

	lshift = 0
	flag = True
	youTurn = 'Seu turno'
	wait =  'Aguarde seu turno'
	textGO = "Fim de jogo"
	textYW = "Vocês ganharam!"

	#print(index, shift)

	server_input.sendall(tip.encode("utf-8"))
	time.sleep(.050)

	while flag:
		
		lshift = shift
		life_str =  str(life_counter)
		server_input.sendall(life_str.encode('utf-8'))
		time.sleep(.200)

		state = str(word)
		server_input.sendall(state.encode("utf-8"))
		time.sleep(.200)

		if life_counter == 0:
			print(textGO)
			print_hangman(life_counter)
			server_input.sendall(textGO.encode('utf-8'))
			flag = False
			end =  True	
		elif '_' not in word:
			print(textYW)
			print_word(word)
			server_input.sendall(textYW.encode('utf-8'))
			flag = False
			end = True		

		elif list_server_input[shift] == server_input:
			#print(shift)
			server_input.sendall(youTurn.encode('utf-8'))
			response = server_input.recv(1024)
			response = response.rstrip()
			print("Mensagem do cliente:", response.decode())
			if response.decode() == 'sair':
				print('Um jogador deixou a sala!')
				list_server_input.remove(server_input)
				index = index-1
				shift = shift-1
				flag = False		
			elif response.decode() in or_word and response.decode() not in word:
				for i in range(0, len(or_word)):
					if response.decode() is or_word[i]:
						word[i] = or_word[i]	
			else:
				life_counter = life_counter - 1

			print_hangman(life_counter)		
			print_word(word)
			if(index != 0):
				shift = (shift+1)%index
			#print(shift)
		else:
			server_input.sendall(wait.encode('utf-8'))
			while lshift == shift and index > 1:
					time.sleep(1)
	if index == 0 :
		end = True
	time.sleep(.200)
	life_str = str(life_counter)
	server_input.sendall(life_str.encode('utf-8'))
	server_input.close()		#break	

#########################################################			

path = './palavras/'
random.seed()
files = os.listdir(path)
i = random.randint(0,len(files)-1)
file_name = path + files[i]
f = open(file_name, 'r')
line_number = random.randint(1, sum(1 for line in f))
word = linecache.getline(file_name, line_number)[0:-1]
print(word)
print('Dica:', files[i][0:-4])
tip = files[i][0:-4]

w = []
for i in range(0, len(word)):
	w.append('_')	
print_word(w)	

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
server_socket.bind(address)
server_socket.listen(15)
server_socket.settimeout(5)

# Print
print('Aguardando conexao para iniciar o jogo, ao fim do jogo o processo será encerrado!')
while not end:
	try:
		server_input, address = server_socket.accept()
		if index < 5 :
			list_server_input.append(server_input)
			print("Nova conexao recebida de ", address)
			thread = threading.Thread(target = thread_management, args = (server_input, w, word, tip))
			thread.start()
			index = index+1
	except socket.timeout:
		pass	
