import socket
import threading
import hashlib


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def brutehack(min,max, hash):
    for i in range(min,max):
        h = hashlib.md5(str(i))
        if h == hash:
            return True

    return False


def connect(sock,port, ip):
    sock.connect((ip,port))
