#
# @Description: Server.py用来进行测试，server2.py用来进行实际的服务端操作
# @Author: Wenjian Lv
# @Date: 2024-12-12
# @LastEditTime: 2024-12-12
#

import socket
import json

def server():
    host = '127.0.0.1'
    port = 54321
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('server is running')


    client_socket, client_address = server_socket.accept()
    print('connect from:', client_address)
    try:
        json_path = 'begin.json'
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            json_str = json.dumps(json_data)
            client_socket.send(json_str.encode('utf-8'))
        
        data_result = client_socket.recv(1024).decode('utf-8')
        print('client send:', data_result)
    except Exception as e:
        print(e)
    finally:
        client_socket.close()
        print('client close')

if __name__ == '__main__':
    server()