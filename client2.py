#
# @Description: Client.py用来进行测试，client2.py用来进行实际的客户端操作
# @Author: Wenjian Lv
# @Date: 2024-12-12
# @LastEditTime: 2024-12-12
#


import socket
import json
from test2 import create_output_json

def client():
    host = '127.0.0.1'
    port = 54321
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print('connect to server')

    data = client_socket.recv(1024)

    if not data:
        return -1
    
    json_data = json.loads(data.decode('utf-8'))    # 首先将接收到的字节数据解码成UTF-8格式的字符串，然后再将其解析转换成字典，该字典可以通过键值对的方式获取数据

    try:
        # for key, value in json_data.items():
        #     print(key, value)

        # print('----------------')
        # print('Identify Instructions Code: ', json_data['identify_instruction_code'])
        # print('HolesNum: ', json_data['HolesNum'])
        # print('Image Path: ', json_data['image_path'])
        for path in json_data['image_path']:
            print(path)
        if len(json_data['image_path']) > 0:
            print(len(json_data['image_path']))
            # result = add()
            # print('result:', result)
            for path in json_data['image_path']:
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

    except json.decoder.JSONDecodeError as e:
        print(e)


if __name__ == '__main__':
    client()