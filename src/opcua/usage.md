# OPC UA サンプルコードの使い方

このドキュメントでは、PythonでOPC UA通信を実装するためのサンプルコードの使い方を説明します。OPC UAサーバーとクライアントをセットアップし、動作確認を行います。

## 前提条件

- Pythonがインストールされていること
- `opcua`ライブラリがインストールされていること

### ライブラリのインストール

まず、`opcua`ライブラリをインストールします。

```bash
pip install opcua
```

## Pythonコードの実行

次に、OPC UAサーバーとクライアントのコードを実行します。

### OPC UAサーバーのコード

以下のコードを`opcua_server.py`という名前で保存します。

```python
from opcua import Server
import time

# サーバーを初期化
server = Server()

# エンドポイントの設定
server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

# 名前空間の追加
uri = "http://examples.freeopcua.github.io"
idx = server.register_namespace(uri)

# オブジェクトを作成
objects = server.get_objects_node()

# 新しいオブジェクトを追加
myobj = objects.add_object(idx, "MyObject")

# 新しい変数を追加
myvar = myobj.add_variable(f"ns={idx};s=MyVariable", "MyVariable", 0)

# 変数の書き込みを許可
myvar.set_writable()

# サーバーを開始
server.start()

try:
    while True:
        # 変数に現在の時刻を設定
        myvar.set_value(time.time())
        time.sleep(1)
finally:
    # サーバーを停止
    server.stop()
```

このコードは、ローカルでOPC UAサーバーを起動し、`MyVariable`という変数ノードを作成して定期的に更新します。

### OPC UAクライアントのコード

以下のコードを`opcua_client.py`という名前で保存します。

```python
from opcua import Client
import time

# クライアントを初期化
client = Client("opc.tcp://localhost:4840/freeopcua/server/")

try:
    # サーバーに接続
    client.connect()

    # ノードを取得
    var = client.get_node("ns=2;s=MyVariable")

    while True:
        # 変数の値を取得
        value = var.get_value()
        print(f"Current value: {value}")
        time.sleep(1)
finally:
    # サーバーとの接続を閉じる
    client.disconnect()
```

このコードは、ローカルのOPC UAサーバーに接続し、`MyVariable`の値を定期的に取得して表示します。

### 実行方法

1. サーバーを実行します。

    ```bash
    python opcua_server.py
    ```

2. 別のターミナルでクライアントを実行します。

    ```bash
    python opcua_client.py
    ```

これで、クライアントがサーバーに接続し、`MyVariable`の値を定期的に取得してコンソールに表示します。

