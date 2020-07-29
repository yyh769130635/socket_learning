# -*- coding: utf-8 -*-
# @Author:peter young
# @file: send_file.py
# @Time: 2020/7/29 19:08


import socket


sk = socket.socket()
ip_port = ("127.0.0.1", 9999)

sk.connect(ip_port)

with open("socket_server.py", "rb") as f:
    for i in f:
        # 数据上传
        sk.send(i)
        # 等待接收完成
        data = sk.recv(1024)
        if data != b"success":
            break

# 给服务器端发送结束信号
sk.send("quit".encode())
