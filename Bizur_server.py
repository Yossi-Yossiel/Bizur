import socket
import hashlib


def distribute(client: socket, count: int, hashcode: str):
    client.send((str(count) + " " + str(count+10000000) + " " + hashcode).encode())
    while True:
        d = client.recv(1024).decode()


hashcode = "EC9C0F7EDCC18A98B1F31853B1813301"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8200))
clients = []
count = 1000000000
i = 0
while True:
    sock.listen()
    clients.append(sock.accept())
    x = clients[i]
    print("client " + str(x[1]) + " decided to be a black slave")
