# use dealer to send/receive messages to/from server

# prepare context, frontend and backend sockets
# while true:
#     poll on both sockets
#     if frontend had input:
#         read all frames from frontend
#         send to backend
#     if backend had input:
#         read all frames from backend
#         send to frontend

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

#  Socket to talk to server
req_context = zmq.Context()
print("Connecting to server...")
socket = req_context.socket(zmq.REQ)
socket.connect("tcp://node00:5555")

while True: 
    message2 = socket.recv()
    print(f'{message}')

    time.sleep(1)

    socket.send(b'hi')

