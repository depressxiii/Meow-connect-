import socket
import threading

pseudo = input("Entrez votre pseudo: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

def receive():
    while True:

        try:
            message = client.recv(1024).decode('utf-8')
            #print('message décodé')
            if message == 'NAME':
                client.send(pseudo.encode('utf-8'))
            else:
                print(message)
            
        except:
            print("Erreur")
            client.close()
            break

def write():
    while True:
        message = f'{pseudo}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
