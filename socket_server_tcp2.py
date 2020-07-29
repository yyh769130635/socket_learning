# -*- coding: utf-8 -*-
# @Author:peter young
# @file: socket_server_tcp2.py
# @Time: 2020/7/29 0:05


import socketserver
import random


class MySever(socketserver.BaseRequestHandler):
    # handle方法出错会报错，setup和finish都会执行
    def setup(self):
        pass

    def handle(self):
        # 定义连接变量
        conn = self.request
        # 发送消息定义
        msg = "hello world!"
        # 发送消息
        conn.send(msg.encode())
        # 进入循环，不断接收客户端消息
        while True:
            data = conn.recv(1024)
            print(data.decode())

            if data == b"exit":
                break
            conn.send(data)
            conn.send(str(random.randint(1, 100)).encode())
        conn.close()

    def finish(self):
        pass


if __name__ == "__main__":
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MySever)
    # 开启异步多线程，等待连接
    server.serve_forever()
