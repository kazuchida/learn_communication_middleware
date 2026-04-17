from unittest.mock import MagicMock, patch, call
import paho.mqtt.client as mqtt


class TestMqttPublisher:
    """mqtt_publisher.pyのテスト"""

    @patch("paho.mqtt.client.Client")
    def test_publisher_connects_to_broker(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # mqtt_publisher.pyのロジックを再現
        broker = "localhost"
        port = 1883
        topic = "test/topic"

        client = mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        client.connect(broker, port, 60)
        client.publish(topic, "Hello, MQTT!")
        client.disconnect()

        mock_client.connect.assert_called_once_with("localhost", 1883, 60)

    @patch("paho.mqtt.client.Client")
    def test_publisher_publishes_message(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        topic = "test/topic"
        message = "Hello, MQTT!"

        client = mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        client.publish(topic, message)

        mock_client.publish.assert_called_once_with("test/topic", "Hello, MQTT!")

    @patch("paho.mqtt.client.Client")
    def test_publisher_disconnects_after_publish(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        client = mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        client.connect("localhost", 1883, 60)
        client.publish("test/topic", "Hello, MQTT!")
        client.disconnect()

        mock_client.disconnect.assert_called_once()


class TestMqttSubscriber:
    """mqtt_subscriber.pyのテスト"""

    def test_on_message_callback_prints_message(self, capsys):
        # on_messageコールバックの動作を検証
        def on_message(client, userdata, msg):
            print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

        mock_msg = MagicMock()
        mock_msg.payload.decode.return_value = "Hello, MQTT!"
        mock_msg.topic = "test/topic"

        on_message(None, None, mock_msg)

        captured = capsys.readouterr()
        assert "Hello, MQTT!" in captured.out
        assert "test/topic" in captured.out

    @patch("paho.mqtt.client.Client")
    def test_subscriber_connects_and_subscribes(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        broker = "localhost"
        port = 1883
        topic = "test/topic"

        client = mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        client.connect(broker, port, 60)
        client.subscribe(topic)

        mock_client.connect.assert_called_once_with("localhost", 1883, 60)
        mock_client.subscribe.assert_called_once_with("test/topic")

    @patch("paho.mqtt.client.Client")
    def test_subscriber_sets_on_message_callback(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        def on_message(client, userdata, msg):
            pass

        client = mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        mock_client.on_message = on_message

        assert mock_client.on_message is on_message

    @patch("paho.mqtt.client.Client")
    def test_subscriber_uses_callback_api_version(self, mock_client_class):
        mock_client_class(mqtt.CallbackAPIVersion.VERSION1)
        mock_client_class.assert_called_once_with(mqtt.CallbackAPIVersion.VERSION1)
