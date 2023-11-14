import socket
import select
import sys
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

client.connect((IP_address, Port))

def receive():
    while True:
        try:
            message = client.recv(2048)
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

threading.Thread(target=receive).start()

while True:
    message = sys.stdin.readline()
    client.send(message.encode())
    sys.stdout.write("<You>")
    sys.stdout.write(message)
    sys.stdout.flush()

client.close()

