import socket

"""
受交换机和路由器设置，广播可能失败
"""
def multicast_sender():
    import struct
    import sys
    message = b'very important data'
    multicast_group = ('224.3.29.71', 10005)
    # Create the datagram socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data
    sock.settimeout(0.2)

    # Set time-to-live for message to 1 so they do not go past the local network segment
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try:
        # Send data to the multicast group
        print('sending {!r}'.format(message))
        sent = sock.sendto(message, multicast_group)

        # look for response from all recipients
        while True:
            print('waiting to receive')
            try:
                data, server = sock.recvfrom(16)
            except socket.timeout as ter:
                print('timeout, no more message', ter)
                break
            else:
                print('received {!r} from {}'.format(data, server))
    finally:
        print('closing socket')
        sock.close()


def recev_mult_msg():
    import socket
    import struct
    import sys
    multicast_group = '0.0.0.0'
    server_address = ('', 10005)

    # Create the socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address.
    sock.bind(server_address)

    # Tell the operating system to add the socket to
    # the multicast group on all interfaces.
    group = socket.inet_aton(multicast_group)
    print(f'group:{group}')
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    print(f'struct.pack mreq: {mreq}')
    sock.setsockopt(socket.IPPROTO_IP,
         socket.IP_ADD_MEMBERSHIP, mreq)

    # Receive/respond loop
    while True:
        print('\n waiting to receive message')
        data, address = sock.recvfrom(1024)
        print('received {} bytes from {}'.format(
            len(data), address))
        print(data)
        print('sending acknowledgement to', address)
        sock.sendto(b'ack', address)


if __name__ == '__main__':
    recev_mult_msg()
