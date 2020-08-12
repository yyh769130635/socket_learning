# -*- coding: utf-8 -*-
# @Author:peter young
# @file: socket_server.py
# @Time: 2020/7/28 22:38


import socket
import random


# 创建实例
sk = socket.socket()

# 定义绑定ip和port
ip_port = ("127.0.0.1", 8888)

# 绑定 监听
sk.bind(ip_port)
# 最大连接数
sk.listen(5)

# 不断循环
while True:
    # 提是信息
    print("正在等待接收数据…………")


    # 接收数据
    conn ,adress = sk.accept()

    msg = "连接成功!"

    # return
    # python3.x以上，网络数据发送接收都是byte类型，若发送str需要编码
    conn.send(msg.encode())

    # 不断接收客户端发来的消息
    while True:
        # 接收客户端数据
        data = conn.recv(1024)
        print(data.decode())
        # 接收到退出指令
        if data == b"exit":
            break
        # 处理客户端数据
        conn.send(data)
        # 发送随机出
        conn.send(str(random.randint(1, 1000)).encode())

    # 主动关闭
    conn.close()