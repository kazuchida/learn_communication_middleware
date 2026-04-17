# MQTT サンプルコードの使い方

このドキュメントでは、PythonでMQTT通信を実装するためのサンプルコードの使い方を説明します。MQTTブローカーには、Mosquittoを使用します。

## 前提条件

- Pythonがインストールされていること
- `paho-mqtt`ライブラリがインストールされていること
- Mosquittoブローカーがローカルで動作していること

### ライブラリのインストール

まず、`paho-mqtt`ライブラリをインストールします。

```bash
pip install paho-mqtt
```

### Mosquittoのインストール

#### macOSの場合
```bash
brew install mosquitto
```

#### Ubuntuの場合
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
```

#### Windowsの場合
1. [Mosquittoの公式サイト](https://mosquitto.org/download/)からWindows用のインストーラーをダウンロードします。
2. ダウンロードしたインストーラーを実行し、インストール手順に従います。

### Mosquittoブローカーの起動

Mosquittoブローカーを起動します。

#### macOS/Linuxの場合
```bash
mosquitto
```

#### Windowsの場合
コマンドプロンプトまたはPowerShellで以下のコマンドを実行します。
```bash
"C:\Program Files\mosquitto\mosquitto.exe"
```

### 動作確認

別のターミナルで、以下のコマンドを実行してローカルのブローカーが正常に動作しているかを確認します。

#### メッセージのパブリッシュ
```bash
mosquitto_pub -h localhost -t test/topic -m "Hello, MQTT!"
```

#### メッセージのサブスクライブ
```bash
mosquitto_sub -h localhost -t test/topic
```

## Pythonコードの実行

次に、Pythonのパブリッシャー（送信側）とサブスクライバー（受信側）のコードを実行します。

### パブリッシャー（送信側）のコード

以下のコードを`mqtt_publisher.py`という名前で保存します。

```python
import paho.mqtt.client as mqtt

# MQTTブローカーの設定
broker = "localhost"
port = 1883
topic = "test/topic"

# MQTTクライアントを作成
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# ブローカーに接続
client.publish(topic, "Hello, MQTT!")

# 接続を終了
client.disconnect()
```

このコードは、MQTTブローカーに接続し、指定したトピックにメッセージを送信します。

### サブスクライバー（受信側）のコード

以下のコードを`mqtt_subscriber.py`という名前で保存します。

```python
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
```

このコードは、MQTTブローカーに接続し、指定したトピックからメッセージを受信して表示します。

### 実行方法

1. サブスクライバーを実行します。

    ```bash
    python mqtt_subscriber.py
    ```

2. 別のターミナルでパブリッシャーを実行します。

    ```bash
    python mqtt_publisher.py
    ```

これで、パブリッシャーが送信したメッセージがサブスクライバーで受信され、コンソールに表示されます。

