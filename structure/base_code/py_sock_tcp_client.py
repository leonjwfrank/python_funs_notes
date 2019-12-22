# Echo client
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening.
server_name = sys.argv[1]   # 外部参数传入服务器名称 , 允许哪个地方访问
# server_address = ('localhost', 10001)   # 默认服务器名称
server_address = (server_name, 10001)

print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # send data
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response.
    amount_received = 0
    amount_expected = len(message)
    datas = b''
    while amount_received < amount_expected:
        data = sock.recv(16)  # 每次接受16字节
        amount_received += len(data)
        print('received {!r}'.format(data))
        datas += data
    print(f'receive data:{type(datas), datas}')
finally:
    print('closing socket')

    sock.close()
