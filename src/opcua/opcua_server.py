from asyncua.sync import Server
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
