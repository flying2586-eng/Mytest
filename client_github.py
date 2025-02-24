#
# @Description: 从https://github.com/flying2586-eng/shanneng.git拉取下来的测试代码 结合了client2.py和server2.py的代码
# @Author: Wenjian Lv
# @Date: 2025-02-24
# @LastEditTime: 2025-02-24
#

import socket
import json
import time
from test2 import create_output_json

def connect_to_server():
    """尝试连接到服务器，如果连接失败，返回 False；成功返回 socket 对象"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 54321))  # 连接服务端
        print("已成功连接到服务器。")
        return client_socket
    except ConnectionRefusedError:
        return None  # 如果无法连接，则返回 None

# 持续尝试连接服务端，直到成功
client_socket = None
while client_socket is None:
    print("服务器未连接，正在尝试连接...")
    client_socket = connect_to_server()
    if client_socket is None:
        time.sleep(5)  # 每隔 5 秒重试一次

# 连接成功后，进行后续通信
try:
    while True:
        try:
            data = client_socket.recv(1024)  # 从服务端接收数据
            if not data:
                print("服务器已断开连接，退出客户端。")
                break  # 服务器断开连接，退出循环

            received_data = json.loads(data.decode('utf-8'))
            print("收到来自服务端的请求:")
            for path in received_data['image_path']:
                print(path)
            if len(received_data['image_path']) > 0:
                print(len(received_data['image_path']))
                for path in received_data['image_path']:
                    result = create_output_json(path)
                    """
                        result = {
                                "identify_state": 200,
                                "image_path": [image_path],
                                "HolesNum": 1,
                                "recognition_result":[
                                    {
                                        "diameter": circle_result[2],
                                        "center_x": circle_result[0],
                                        "center_y": circle_result[1]
                                    }
                                ]
                            }
                    """
                if result is not None:
                    # 将json_data发送到服务器
                    client_socket.send(str(result).encode('utf-8'))
                else:
                    raise Exception('result is None')
            else:
                raise Exception('image_path is None')

        except json.JSONDecodeError:
            print("收到的数据格式不正确，忽略。")

        except ConnectionResetError:
            print("连接被服务器重置，退出客户端。")
            break  # 服务器重置连接，客户端退出

except KeyboardInterrupt:
    print("客户端手动终止。")

finally:
    client_socket.close()
    print("客户端已关闭。")