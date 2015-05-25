'''
Demo of using udp to send and recieve packets

usage: python udp_echp.py port_num

TODO make asynchronous

TODO use STUN addresses rather than localhost


'''
import socket
import sys
import threading
import config

them = config.them

my_ip,my_port= sys.argv[1], int(sys.argv[2])

def listen():
    while True:
        msg = sock.recv(1024)
        if len(msg) and msg[-1] !='\n':
          msg = '\n' + msg #+'\n'
        print msg

def send(sock,msg):
    num_sent = sock.sendto(msg,them)

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((my_ip,my_port))

t = threading.Thread(None,listen)
t.start()

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
while True:
    msg = raw_input('> ')
    send(msg)