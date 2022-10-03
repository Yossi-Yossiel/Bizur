import multiprocessing
import socket
import threading
import hashlib

coresnum = multiprocessing.cpu_count()
port = 8200
ip = input("ip:")
event = threading.Event()


def brutehack(min, max, hash, sock: socket.socket ):
    i = min
    while not event.is_set() and i < max:
        h = hashlib.md5(str(i).encode()).hexdigest()
        if h == hash:
            print("found " + str(i))
            sock.send(("found " + str(i)).encode())
            event.set()
            return 0
        i += 1


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    char = int(sock.recv(1024).decode())
    sock.send(("got the char length " + str(char)).encode())
    data = sock.recv(char).decode()  # should receive 3 params: min, max and hash code
    sock.send("ok".encode())
    d1 = sock.recv(char).decode()
    if d1 == data:
        sock.send("good".encode())
        data = data.split()
        min = int(data[0])
        max = int(data[1])
        hashcode = data[2]
    else:
        sock.send("send again".encode())
        d2 = sock.recv(char)
        if d2 == d1:
            sock.send("good".encode())
            min = int(d1[0])
            max = int(d1[1])
            hashcode = d1[2]
        elif d2 == data:
            sock.send("good".encode())
            min = int(data[0])
            max = int(data[1])
            hashcode = data[2]
        else:
            sock.send("nope".encode())
            min = 0
            max = 0
            hashcode = "Error"
            sock.close()
    mmlist = []
    mmlist.append(min)
    for i in range(coresnum):

        min = min + ((max-min)//coresnum)
        mmlist.append(min)
    tlist = []
    for i in range(len(mmlist)-1):
        t = threading.Thread(target=brutehack, args=(mmlist[i],mmlist[i+1],hashcode, sock))
        t.start()
        tlist.append(t)
    for i in tlist:
        i.join()
    while not event.is_set():
        sock.send("nope".encode())
        if threading.active_count() == 1:
            sock.close()
            main()


main()
