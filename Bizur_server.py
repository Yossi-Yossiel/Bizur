import socket
import hashlib
import threading


def ThreadListen(client: socket.socket):
    flag = client.recv(1024).decode().split()
    if flag[0] == "found":
        print(flag)
        return


def distribute(client: socket.socket, count: int, hashcode: str):
    count1 = count + 10000000
    send_c = str(count) + " " + str(count1) + " " + hashcode
    length = str(len(send_c))
    print(length)
    client.send(length.encode())
    print(client.recv(1024).decode())
    client.send(send_c.encode())
    d = client.recv(1024).decode()
    if d == "ok":
        client.send(send_c.encode())
        d = client.recv(1024).decode()
        if d == "good":
            return True,count
        elif d == "send again":
            client.send(send_c.encode())
            d = client.recv(1024)
            if d == "good":
                return True,count
            else:
                return False,count


hashcode = hashlib.md5("1000000010".encode()).hexdigest() #"EC9C0F7EDCC18A98B1F31853B1813301".lower()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8200))
clients = []
count = 1000000000
i = 0
tlist = []
while True:
    sock.listen()
    clients.append(sock.accept())
    x = clients[i]
    client = x[0]
    print("client " + str(x[1]) + " decided to be a black slave")
    workFlag,count = distribute(client,count,hashcode)
    if not workFlag:
        print("could not send the info, closing connection")
        client.close()
    t = threading.Thread(target=ThreadListen, args=(client,))
    t.start()
    tlist.append(t)

    print(workFlag)
    i += 1
