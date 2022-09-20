import socket
import hashlib

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
