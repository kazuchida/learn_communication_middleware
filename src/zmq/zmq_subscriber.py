import zmq

# ZeroMQコンテキストを作成
context = zmq.Context()

# ソケットを作成し、接続
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

# 全てのメッセージを受信するためのフィルタを設定
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    # メッセージを受信
    message = socket.recv_string()
    print(f"Received message: {message}")
