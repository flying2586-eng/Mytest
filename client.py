#
 # @func 通过tcp连接json数据,并对其进行解析，当全部接受完毕后，开启新的函数
 # @desc 
 # @param {}  
 # @return {} 
#
import socket
import json

def add(a = 1, b = 2):
    c = a + b
    # c = None
    return c

def test1(path: str):
    print(path)

def client():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print('connect to server')

    while True:
        message = input('please enter start (exit):')
        if message == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024)
        
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
                result = add()
                print('result:', result)
                for path in json_data['image_path']:
                    test1(path)
                if result is not None:
                    client_socket.send(str(result).encode('utf-8'))
                else:
                    raise Exception('result is None')
            else:
                raise Exception('image_path is None')

        except json.decoder.JSONDecodeError as e:
            print(e)
    
    client_socket.close()
    print('client close')

if __name__ == '__main__':
    client()