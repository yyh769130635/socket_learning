# -*- coding: utf-8 -*-
# @Author:peter young
# @file: socket_client.py
# @Time: 2020/7/28 22:48


import socket

# 创建实例
client = socket.socket()

# 访问服务器端的ip和端口
ip_port = ("127.0.0.1", 8888)

# 连接主机
client.connect(ip_port)


# 定义一个循环，不断地发送消息
while True:
    # 接收主机信息
    data = client.recv(1024)

    # 打印接收的数据
    print(data.decode())

    # 输入发送的消息
    msg_input = input("请输入要发送的消息：")
    # 发送消息
    client.send(msg_input.encode())
    # 退出循环
    if msg_input=="exit":
        break
    data = client.recv(1024)
    print((data.decode()))