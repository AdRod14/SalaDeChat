import socket
import select
import sys
import threading


def clientthread(conn):
    conn.send("Has ingresado al chat!!!".encode('ascii'))
    while True:
        try:
            message = conn.recv(2048).decode('ascii')
            print("<" + dictionary_of_clients[conn] + "> " + message)
            message_to_send = "<" + dictionary_of_clients[conn] + "> " + message
            broadcast(message_to_send.encode('ascii'), dictionary_of_clients[conn])
        except:
            conn.close()
            remove(conn)
            break


def broadcast(message, sender):
    for conn in dictionary_of_clients:
        if dictionary_of_clients[conn] != sender:
            conn.send(message)


def remove(connection):
    if connection in dictionary_of_clients:
        del dictionary_of_clients[connection]


def receive():
    while True:
        conn, addr = server.accept()
        remote_address = conn.getpeername()
        remote_port = remote_address[1]
        print(str(remote_port) + " connected")
        conn.send("Ingresa tu nombre de usuario: ".encode('ascii'))
        apodo = conn.recv(2048).decode('ascii')
        dictionary_of_clients[conn] = apodo
        broadcast(f"{apodo} se ha unido al chat grupal.".encode("ascii"), apodo)
        threading.Thread(target=clientthread, args=(conn,)).start()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
dictionary_of_clients = {}

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.bind((IP_address, Port))
server.listen(100)

receive()


