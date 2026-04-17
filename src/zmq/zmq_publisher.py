import zmq
import time

# ZeroMQコンテキストを作成
context = zmq.Context()

# ソケットを作成し、バインド
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    # メッセージを送信
    message = "Hello, ZeroMQ!"
    print(f"Sending message: {message}")
    socket.send_string(message)
    time.sleep(1)