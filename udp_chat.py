# -*- coding: utf-8 -*-
# @Time : 8/12/2020 4:31 PM
# @Author : Peter yang
import socket


def send_msg(udp_socket):
    """发送消息"""
    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))
    # 从键盘获取数据
    send_data = input("请输入要发送的数据")
    # 用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    # 接收回送过来的数据
    # recv_data = udp_socket.recvfrom(1024)
    recv_data = udp_socket.recv(1024)
    print("%s: %s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("127.0.0.1", 8888))
    # 循环来进行处理
    while True:
        print("------聊天器------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op = input("请输入功能:")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("wrong input!! 重新输入...")

    udp_socket.close()


if __name__ == "__main__":
    main()
