import paho.mqtt.client as mqtt

# MQTTブローカーの設定
broker = "localhost"
port = 1883
topic = "test/topic"

# MQTTクライアントを作成
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# ブローカーに接続
client.connect(broker, port, 60)

# メッセージをパブリッシュ
client.publish(topic, "Hello, MQTT!")

# 接続を終了
client.disconnect()
