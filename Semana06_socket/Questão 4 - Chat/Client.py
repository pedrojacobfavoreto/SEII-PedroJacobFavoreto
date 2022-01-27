import socket # Importa biblioteca
import threading # Importa biblioteca
import time # Importa biblioteca

PORT = 5050 # Defini a porta
FORMATO = 'utf-8' # Determina o formato das mensagens
SERVER = "127.0.1.1" # Especifica o IP do servidor
ADDR = (SERVER, PORT) # Determina a Tupla do endereço

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket padrão para TCP
client.connect(ADDR) # Conecta com o servidor

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode() # Recebe as mensagens
        mensagem_splitada = msg.split("=") # Separa a mensagem
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2]) # Mostra quem enviou a mensagem

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO)) # Envia a mensagem codificada para o servidor

def enviar_mensagem():
    mensagem = input() # Coleta a mensagem do cliente
    enviar("msg=" + mensagem) # Envia a mensagem do cliente

def enviar_nome():
    nome = input('Digite seu nome: ') # Coleta o nome do cliente
    enviar("nome=" + nome) # Envia o nome do cliente

def iniciar_envio():
    enviar_nome() # Envia o nome do cliente
    enviar_mensagem() # Envia mensagem do cliente

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens) # Determina a Thread para receber mensagens
    thread2 = threading.Thread(target=iniciar_envio) # Determina a Thread para enviar as mensagens dos clientes
    
    # Inicia as threads
    thread1.start()
    thread2.start()

iniciar()