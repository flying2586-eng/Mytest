#
# @Description: 从https://github.com/flying2586-eng/shanneng.git拉取下来的测试代码
# @Author: Wenjian Lv
# @Date: 2025-02-24
# @LastEditTime: 2025-02-24
#

import socket
import json
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
server_socket.bind(('127.0.0.1', 54321)) 
server_socket.listen(1) 

print("服务端等待客户端连接...")

client_socket, client_address = server_socket.accept()
print(f"客户端 {client_address} 已连接")

try:
    while True:
        with open('begin.json', 'r') as f:
            data = json.load(f)
        json_data = json.dumps(data).encode('utf-8')
        client_socket.sendall(json_data)
        print("已发送数据到客户端:", json.dumps(data, indent=4))
        try:
            response = client_socket.recv(1024)
            if response:
                try:
                    response_data = json.loads(response.decode('utf-8'))
                    print("收到来自客户端的 JSON 响应:")
                    print(json.dumps(response_data, indent=4))
                except json.JSONDecodeError:
                    print("收到来自客户端的消息:", response.decode('utf-8'))
            else:
                print("客户端断开连接，退出循环。")
                break
        except ConnectionResetError:
            print("客户端连接被重置，等待重新连接...")
            break
        time.sleep(5)

except KeyboardInterrupt:
    print("服务器手动终止。")

finally:
    client_socket.close()
    server_socket.close()
    print("服务器已关闭。")