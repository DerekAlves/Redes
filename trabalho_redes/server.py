#!/usr/bin/python

import socket
import threading


def print_word(word):
	for letter in word:
		print(letter, end = " ")
	print('\n')		

address = ("localhost", 20000)

#manages each thread received
def thread_management(server_input, word, or_word):
	
	print_word(word)
	while True:
		response = server_input.recv(1024)
		response = response.rstrip()
		if (response.decode() != "sair"):
			print("Mensagem do cliente:", response.decode())			
			if response.decode() in or_word:
				for i in range(0, len(or_word)):
					if response.decode() is or_word[i]:
						word[i] = or_word[i]			
			else:
				print('-1')	
			print_word(word)				
		else:
			server_input.close()
			break
	

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
server_socket.bind(address)
server_socket.listen(15)

f = open('./palavras.txt', 'r')
word = f.readlines()[0][0:-1]
print(word)

w = []
for i in range(0, len(word)):
	w.append('_')	

# Print
while True:
	server_input, address = server_socket.accept()
	print("Nova conexao recebida de ", address)
	thread = threading.Thread(target = thread_management, args = (server_input, w, word))
	thread.start()



