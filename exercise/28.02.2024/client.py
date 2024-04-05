import time

import cv2
import socket
import numpy as np
import struct


class Camera(object):
    # 摄像头类，采集视频，发送到服务器

    # 创建类时打开摄像头
    def __init__(self, dest_ip, dest_port):
        # 打开摄像头
        self.myVC = cv2.VideoCapture(0)

        # 创建套接字（用于主机与服务器端通讯）
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 连接服务器
        self.client_socket.connect((dest_ip, dest_port))

        # 定义了压缩后图片的绝对大小，160x120
        self.resolution = (1024, 720)

    def run(self):
        try:
            # 循环发送图片
            while True:
                # 采集摄像头
                # 参数check为是否捕获成功，参数img为捕获影像
                # myVC.read()返回两个值
                check, img = self.myVC.read()

                # 压缩图片

                # 重置图片大小（防止摄像头拍出来的图片默认大小不同）
                img = cv2.resize(img, self.resolution)
                # 将img图片压缩为jpg格式(_, 指的是他第一个返回值用不上，丢弃了）
                _, img_encode = cv2.imencode('.jpg', img)
                # 转换为numpy格式数据
                img_code = np.array(img_encode)
                # 生成对应的二进制数据
                img_date = img_code.tobytes()

                # 打印传输图片的数据大小
                print("Transmitting image data size:", len(img_date))

                # 发送到服务器
                # i 表示4个字节，h 表示2个字节
                # ihh表示 1 2 3 个参数分别为 4 2 2 字节
                # 参数1传图片大小，参数2传图片宽度，参数3传图片高度，参数4传图片本身
                # struct是python提供的传定长数据（在此处为了让服务端分开哪到哪的数据为一张图片
                # 这里为什么要try呢？因为发送的图片过大会导致发送失败
                try:
                    self.client_socket.send(
                        struct.pack("ihh", len(img_date), self.resolution[0], self.resolution[1]) + img_date)
                except Exception as e:
                    print("Error sending data:", e)
                    continue  # 继续当前循环
                # time.sleep(0.1)
        except KeyboardInterrupt:
            # 按下按键退出程序
            pass

    def __del__(self):
        # 释放摄像头资源
        self.myVC.release()

        # 关闭套接字
        self.client_socket.close()


# 定义主函数
def main():
    # 1. 获取链接的tcp服务器的IP
    dest_ip = input("请输入服务器IP：")
    dest_ip = dest_ip if dest_ip else "127.0.0.1"

    # 2. 获取tcp服务器的端口
    dest_port = input("请输入服务器的端口：")
    dest_port = int(dest_port) if dest_port else 54609

    # 3. 创建Camera对象
    camera = Camera(dest_ip, dest_port)

    # 4. 调用对象run方法，为服务器传送摄像头数据
    camera.run()

    pass


if __name__ == '__main__':
    main()
