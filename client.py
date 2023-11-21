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
            else:
                print(message)
        except:
            print("Ha ocurrido un error!")
            client.close()
            break


def write():
    while True:
        message = sys.stdin.readline()
        if message == "/exit":
            print("Vuelve pronto")
            client.close()
            sys.exit()
        client.send(message.encode('ascii'))
        sys.stdout.write("<You>")
        sys.stdout.write(message)
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

