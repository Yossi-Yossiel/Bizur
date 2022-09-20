import socket
import hashlib


def distribute(client: socket.socket, count: int, hashcode: str):
    sendc = str(count) + " " + str(count+10000000) + " " + hashcode
    client.send(str((len(sendc))))
    client.send(sendc.encode())
    d = client.recv(1024).decode()
    if d == "ok":
        client.send(sendc.encode())
        d = client.recv(1024).decode()
        if d == "good":
            return True
        elif d == "send again":
            client.send(sendc.encode())
            d = client.recv(1024)
            if d == "good":
                return True
            else:
                return False


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
    if not distribute():

    i += 1
