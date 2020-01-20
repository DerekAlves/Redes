SERVIDOR:
Para rodar o servidor: $python3 server.py

Você irá perceber as seguintes mensagens: 
   <Palavra secreta> Ex: "paraguai"
   <Dica que será enviada ao cliente> Ex: "Dica: País"
   "Aguardando conexao para iniciar o jogo, ao fim do jogo o processo será encerrado!"
  
Conforme as jogadas forem sendo feitas, irá ser apresentado o estado atual do jogo no servidor.

Obs: Para rodar o servidor, o arquivo server.py precisa estar no mesmo diretório que a pasta 'palavras' que contém diversos arquivos .txt com as palavras a serem sorteadas para o jogo.
     O servidor está limitado a 5 conexões de clientes com uso de Threads, mais conexões podem ser abertas com uma pequena alteração no código.

CLIENTE:
Para rodar o servidor: $python3 client.py

Não é necessário arquivos extras para a execução do cliente.

Ao executar, será apresentada a seguinte mensagem:
  "1 para localhost ou forneça um IP válido para conectar a um servidor: "
Para se conectar o cliente a um servidor que esteja operando em outra máquina, ambos devem estar conectado à mesma rede.
Após conectar cliente, será apresentada a dica:
  Ex: "Dica: País"
E o estado do jogo.

Caso seja seu turno, será apresentado: 
  "Seu turno"
  "Informe texto ou digite 'sair' para desconectar: " Se sair, a conexão será encerrada, senão a mensagem será enviada para o servidor.

Caso contrário:
  "Aguarde seu turno", o jogador não deve tentar efetuar uma jogada fora de sua vez.
  
Caso o jogo seja vencido, será apresentado:
  "Vocês Ganharam"
  Caso contrário:
  "Fim de Jogo"
E a conexão será encerrada no servidor, e clientes.
