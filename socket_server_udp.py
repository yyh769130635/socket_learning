# -*- coding: utf-8 -*-
# @Author:peter young
# @file: socket_server_udp.py
# @Time: 2020/7/28 23:23


import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ("127.0.0.1", 8888)

sk.bind(ip_port)

while True:
    data = sk.recv(1024)

    print(data.decode())