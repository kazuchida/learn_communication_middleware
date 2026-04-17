import paho.mqtt.client as mqtt

# MQTTブローカーの設定
broker = "localhost"
port = 1883
topic = "test/topic"

# メッセージ受信時のコールバック関数
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# MQTTクライアントを作成
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# コールバック関数を設定
client.on_message = on_message

# ブローカーに接続
client.connect(broker, port, 60)

# トピックをサブスクライブ
client.subscribe(topic)

# 無限ループで待機
client.loop_forever()
