import socket
import json

#
 # @func server
 # @desc 发送json数据到客户端
 # @param {}  
 # @return {} 
#

def server():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print('server is running')

    while True:
        client_socket, client_address = server_socket.accept()
        print('connect from:', client_address)
        try:
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    msg = data.decode('utf-8').strip()
                    print('client send:', msg)
                    if msg == 'start':
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
                            send_msg = 'error, please enter start again'
                            client_socket.send(send_msg.encode('utf-8'))
                    else:
                        send_msg = 'error, please enter start'
                        client_socket.send(send_msg.encode('utf-8'))
                except Exception as e:
                    print(e)
                    break
        except Exception as e:
            print(e)
        finally:
            client_socket.close()
            print('client close')

if __name__ == '__main__':
    server()