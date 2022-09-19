import multiprocessing
import socket
import threading
import hashlib


def brutehack(min,max, hash, sock):
    for i in range(min,max+1):
        h = hashlib.md5(str(i).encode()).hexdigest()
        if h == hash:
            sock.send(("found " + str(i)).encode())



def main():
    coresnum = multiprocessing.cpu_count()
    port = int(input("port:"))
    ip = input("ip:")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    char = int(sock.recv(1024))
    data = sock.recv(char).decode()  # should receive 3 params: min, max and hash code
    sock.send("ok".encode())
    d1 = sock.recv(1024).decode()
    if d1 == data:
        data = data.split()
        min = data[0]
        max = data[1]
        hashcode = data[2]
    else:
        sock.send("send again".encode())
        d2 = sock.recv(char)
        if d2 == d1:
            min = d1[0]
            max = d1[1]
            hashcode = d1[2]
        elif d2 == data:
            min = data[0]
            max = data[1]
            hashcode = data[2]
        else:
            sock.send("nope".encode())
            min = 0
            max = 0
            hashcode = "Error"
    mmlist = []
    mmlist.append(min)
    for i in range(coresnum):
        n = max // coresnum + (max//coresnum)*i
        mmlist.append(n)

    tlist = []
    for i in range(mmlist-1):
        t = threading.Thread(target=brutehack, args=(mmlist[i],mmlist[i+1],hashcode,sock))
        t.start()
        tlist.append(t)
    for i in tlist:
        i.join()
    sock.close()

main()
