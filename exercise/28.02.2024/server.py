from flask import Flask, render_template, Response
import socket
import cv2
import numpy as np
import struct

app = Flask(__name__)

# 创建一个UDP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 0))  # 绑定本地所有IP地址的随机端口

# 获取绑定后的端口号
port = server_socket.getsockname()[1]
print(f"Server is running on port {port}")

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


def gen():
    """生成器函数，用于获取视频流"""
    while True:
        # 接收数据包
        data, addr = server_socket.recvfrom(65507)

        # 解包数据
        size, width, height = struct.unpack('ihh', data[:8])

        # 重构图像
        img_decode = np.fromstring(data[8:], dtype=np.uint8)
        img = cv2.imdecode(img_decode, cv2.IMREAD_COLOR | cv2.IMREAD_ANYDEPTH)

        # 编码图像
        ret, jpeg = cv2.imencode('.jpg', img)

        # 构建帧数据
        frame = jpeg.tobytes()

        # 生成multipart/x-mixed-replace格式的数据
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    """视频流路由"""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)