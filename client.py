import socket
import select
import sys
import threading


def receive():
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message.startswith("Ingresa tu nombre de usuario: "):
                client.send(apodo.encode('ascii'))
            elif message.startswith("Has salido del chat."):
                client.close()
                break
            else:
                print(message)
        except:
            print("Ha ocurrido un error.")
            client.close()
            break


def write():
    while True:
        message = sys.stdin.readline().strip()
        client.send(message.encode('ascii'))
        if message == "/end" or "":
            break
        sys.stdout.write("<You>")
        sys.stdout.write(message + "\n")
        sys.stdout.flush()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

apodo = input("Ingresa un nombre de usuario: ")

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

client.connect((IP_address, Port))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()

