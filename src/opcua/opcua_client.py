from asyncua.sync import Client
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
