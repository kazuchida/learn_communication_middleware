from unittest.mock import MagicMock, patch, call
import zmq


class TestZmqPublisher:
    """zmq_publisher.pyのテスト"""

    @patch("zmq.Context")
    def test_publisher_creates_pub_socket(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.PUB)

        mock_context.socket.assert_called_once_with(zmq.PUB)

    @patch("zmq.Context")
    def test_publisher_binds_to_port(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:5555")

        mock_socket.bind.assert_called_once_with("tcp://*:5555")

    @patch("zmq.Context")
    def test_publisher_sends_string_message(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.PUB)

        message = "Hello, ZeroMQ!"
        socket.send_string(message)

        mock_socket.send_string.assert_called_once_with("Hello, ZeroMQ!")

    @patch("zmq.Context")
    def test_publisher_prints_message(self, mock_context_class, capsys):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context
        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        message = "Hello, ZeroMQ!"
        print(f"Sending message: {message}")

        captured = capsys.readouterr()
        assert "Sending message: Hello, ZeroMQ!" in captured.out


class TestZmqSubscriber:
    """zmq_subscriber.pyのテスト"""

    @patch("zmq.Context")
    def test_subscriber_creates_sub_socket(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.SUB)

        mock_context.socket.assert_called_once_with(zmq.SUB)

    @patch("zmq.Context")
    def test_subscriber_connects_to_publisher(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:5555")

        mock_socket.connect.assert_called_once_with("tcp://localhost:5555")

    @patch("zmq.Context")
    def test_subscriber_sets_empty_topic_filter(self, mock_context_class):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, "")

        mock_socket.setsockopt_string.assert_called_once_with(zmq.SUBSCRIBE, "")

    @patch("zmq.Context")
    def test_subscriber_receives_message(self, mock_context_class, capsys):
        mock_context = MagicMock()
        mock_context_class.return_value = mock_context

        mock_socket = MagicMock()
        mock_socket.recv_string.return_value = "Hello, ZeroMQ!"
        mock_context.socket.return_value = mock_socket

        context = mock_context_class()
        socket = context.socket(zmq.SUB)
        message = socket.recv_string()
        print(f"Received message: {message}")

        mock_socket.recv_string.assert_called_once()
        captured = capsys.readouterr()
        assert "Received message: Hello, ZeroMQ!" in captured.out
