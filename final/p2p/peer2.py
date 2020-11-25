import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:

    msg = socket.recv_string()
    print('from peer1: ', msg)

    new_msg = input('msg: ')
    socket.send_string(new_msg)




