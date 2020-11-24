import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#  Socket to talk to server
print("Connecting to server...")
req_context = zmq.Context()
socket = req_context.socket(zmq.REQ)
socket.connect("tcp://node01:5556")

while True:
    socket.send(b'message')

    time.sleep(1)

    message1 = socket.recv()
    print(f'{message}')
 