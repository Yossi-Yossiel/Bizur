import socket
import threading
import hashlib

port = input("port:")
ip = input("ip:")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((ip, port))


def brutehack(min,max, hash):
    for i in range(min,max):
        h = hashlib.md5(str(i))
        if h == hash:
            return True

    return False
