# -*- coding: utf-8 -*-
# @Author:peter young
# @file: socket_client_udp.py
# @Time: 2020/7/28 23:23

import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8888)

while True:
    msg_input = input("请输入数据：")

    if msg_input=="exit":
        break

    sk.sendto(msg_input.encode(),ip_port)

sk.close()