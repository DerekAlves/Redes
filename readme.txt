SERVIDOR:
Para rodar o servidor: $python3 server.py

Você irá perceber as seguintes mensagens: 
  "paraguai" -> indica a palavra secreta
  "Dica: País" -> dica que será enviada para o cliente.
  "Aguardando conexao para iniciar o jogo, ao fim do jogo o processo será encerrado!"
  
Conforme as jogadas forem sendo feitas, irá ser apresentado o estado atual do jogo no servidor.

Obs: Para rodar o servidor, o arquivo server.py precisa estar do lado da pasta 'palavras' que contém diversos arquivos .txt com as palavras
     O servidor está limitado a 5 conexões com uso de Threads, mais conexões podem ser abertas com uma pequena alteração no código.
CLIENTE:
Para rodar o servidor: $python3 client.py

Não é necessário arquivos extras para a execução do cliente.

Ao executar, será apresentada a seguinte mensagem:
  "1 para localhost ou forneça um IP válido para conectar a um servidor: "
Após conectar cliente, será apresentado a dica:
  "Dica: País"
E o estado do jogo.

Caso seja seu turno, será apresentado: 
  "Seu turno"
  "Informe texto ou digite 'sair' para desconectar: " Se sair, a conexão será encerrada, se não a mensagem será enviada para o servidor

Caso contrário:
  "Aguarde seu turno", recomenda-se que o jogador não tente efetuar sua jogada fora de sua vez, uma exception poderá ser levantada.
  
  Caso o jogo seja vencido, será apresentado:
  "Vocês Ganharam"
  Caso contrário:
  "Fim de Jogo"
E a conexão será encerrada no servidor, e clientes.
