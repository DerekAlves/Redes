#!/usr/bin/python

import socket
import threading
import os
import random
import linecache

def print_word(word):
	for letter in word:
		print(letter, end = " ")
	print('\n')		

address = ("localhost", 20000)

#manages each thread received
def thread_management(server_input, word, or_word):
	life_counter = 6
	while True:
		response = server_input.recv(1024)
		response = response.rstrip()
		if response.decode() != "sair":
			print("Mensagem do cliente:", response.decode())			
			if response.decode() in or_word:
				for i in range(0, len(or_word)):
					if response.decode() is or_word[i]:
						word[i] = or_word[i]			
			else:
				life_counter = life_counter - 1
				print(life_counter)	
			if life_counter == 0:
				print('GAME OVER')
				server_input.close()
				break		
			print_word(word)				
		else:
			server_input.close()
			break

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
while True:
	server_input, address = server_socket.accept()
	print("Nova conexao recebida de ", address)
	thread = threading.Thread(target = thread_management, args = (server_input, w, word))
	thread.start()



