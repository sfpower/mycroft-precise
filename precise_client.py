#!/usr/bin/env python3

import socket
import sys
from precise_runner import PreciseRunner, PreciseEngine, ReadWriteStream
import time

ADDRESS = ('localhost', 10000)
CHUNK_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDRESS)

print(sock.getsockname()[1])

stream = ReadWriteStream()

try:
    while True:
    	print(sock.getsockname()[1])
    	stream.write(sys.stdin.buffer.read(2048))
    	sock.sendall(stream.read(CHUNK_SIZE))
finally:
    sock.close()


