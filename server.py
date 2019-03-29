import socket
# from socket import *

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Escutar a porta 9000
server = sock.bind(('localhost', 9000))

# Definir o limite de 1 conexao paralela
sock.listen(1)

# Aceitar uma conexao e finaliza-la
mensagem = "Ola Cliente"
tamanho_da_mensagem = len(mensagem)
print("Tamanho da mensagem = {}".format(len(mensagem)))

while True:
    # Aguardar uma conexao
    print("Aguardando conexao")
    connection, address_client = sock.accept()    
    
    # Envio tamanho da mensagem
    connection.sendall(str(tamanho_da_mensagem).zfill(4).encode())
    
    # Enviar mensagem
    connection.sendall(mensagem.encode())

    # Aguardar tamanho da mensagem
    expected_data_size = ''
    while(expected_data_size == ''):
        expected_data_size += connection.recv(4).decode()
    expected_data_size = int(expected_data_size)

    received_data = ''
    while len(received_data) < expected_data_size:
        # Ler o dado recebido
        received_data += connection.recv(4).decode()
        print("Tamanho do dado {}".format(len(received_data)))
    print(received_data)

    # Finalizar a conexao
    connection.close()
