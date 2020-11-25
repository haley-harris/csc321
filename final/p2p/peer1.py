import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://node00:5555")

while True:

    msg = input('msg: ')
    socket.send_string(msg)
    print('sending ', msg)

    new_msg = socket.recv_string()
    print('from peer2: ', new_msg)
