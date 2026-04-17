# ZeroMQ サンプルコードの使い方

このドキュメントでは、PythonでZeroMQ通信を実装するためのサンプルコードの使い方を説明します。ZeroMQはブローカーレスのメッセージングライブラリで、専用のメッセージブローカーなしにパブリッシャー・サブスクライバー通信が可能です。

## 前提条件

- Pythonがインストールされていること
- `pyzmq`ライブラリがインストールされていること

### ライブラリのインストール

まず、`pyzmq`ライブラリをインストールします。

```bash
pip install pyzmq
```

## Pythonコードの実行

次に、ZeroMQのパブリッシャー（送信側）とサブスクライバー（受信側）のコードを実行します。

### パブリッシャー（送信側）のコード

以下のコードを`zmq_publisher.py`という名前で保存します。

```python
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
```

このコードは、TCPポート5555でPUBソケットを起動し、1秒ごとにメッセージを送信し続けます。

### サブスクライバー（受信側）のコード

以下のコードを`zmq_subscriber.py`という名前で保存します。

```python
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
```

このコードは、パブリッシャーのポート5555に接続し、受信したメッセージをコンソールに表示します。`zmq.SUBSCRIBE`に空文字列を設定することで、全てのトピックのメッセージを受信します。

### 実行方法

1. パブリッシャーを実行します。

    ```bash
    python zmq_publisher.py
    ```

2. 別のターミナルでサブスクライバーを実行します。

    ```bash
    python zmq_subscriber.py
    ```

これで、パブリッシャーが送信したメッセージがサブスクライバーで受信され、コンソールに表示されます。

> **注意**: ZeroMQのPUB/SUBパターンでは、サブスクライバーの接続直後に送信されたメッセージは受信できない場合があります（スロースタート問題）。テスト時はパブリッシャーを起動する前にサブスクライバーを起動するか、パブリッシャー側に短い待機時間を設けることを推奨します。
