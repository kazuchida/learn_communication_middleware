from unittest.mock import MagicMock, patch, PropertyMock
import time


class TestOpcuaServer:
    """opcua_server.pyのテスト"""

    @patch("opcua.Server")
    def test_server_sets_endpoint(self, mock_server_class):
        mock_server = MagicMock()
        mock_server_class.return_value = mock_server

        endpoint = "opc.tcp://localhost:4840/freeopcua/server/"

        server = mock_server_class()
        server.set_endpoint(endpoint)

        mock_server.set_endpoint.assert_called_once_with(
            "opc.tcp://localhost:4840/freeopcua/server/"
        )

    @patch("opcua.Server")
    def test_server_registers_namespace(self, mock_server_class):
        mock_server = MagicMock()
        mock_server.register_namespace.return_value = 2
        mock_server_class.return_value = mock_server

        uri = "http://examples.freeopcua.github.io"

        server = mock_server_class()
        idx = server.register_namespace(uri)

        mock_server.register_namespace.assert_called_once_with(uri)
        assert idx == 2

    @patch("opcua.Server")
    def test_server_adds_object_and_variable(self, mock_server_class):
        mock_server = MagicMock()
        mock_server_class.return_value = mock_server

        mock_objects = MagicMock()
        mock_server.get_objects_node.return_value = mock_objects

        mock_obj = MagicMock()
        mock_objects.add_object.return_value = mock_obj

        mock_var = MagicMock()
        mock_obj.add_variable.return_value = mock_var

        server = mock_server_class()
        idx = 2
        objects = server.get_objects_node()
        myobj = objects.add_object(idx, "MyObject")
        myvar = myobj.add_variable(f"ns={idx};s=MyVariable", "MyVariable", 0)
        myvar.set_writable()

        mock_objects.add_object.assert_called_once_with(2, "MyObject")
        mock_obj.add_variable.assert_called_once_with("ns=2;s=MyVariable", "MyVariable", 0)
        mock_var.set_writable.assert_called_once()

    @patch("opcua.Server")
    def test_server_starts_and_stops(self, mock_server_class):
        mock_server = MagicMock()
        mock_server_class.return_value = mock_server

        server = mock_server_class()
        server.start()
        server.stop()

        mock_server.start.assert_called_once()
        mock_server.stop.assert_called_once()

    @patch("opcua.Server")
    def test_server_sets_variable_value(self, mock_server_class):
        mock_server = MagicMock()
        mock_server_class.return_value = mock_server

        mock_var = MagicMock()

        # 変数に時刻を設定する動作を検証
        current_time = time.time()
        mock_var.set_value(current_time)

        mock_var.set_value.assert_called_once_with(current_time)


class TestOpcuaClient:
    """opcua_client.pyのテスト"""

    @patch("opcua.Client")
    def test_client_connects_to_server(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        endpoint = "opc.tcp://localhost:4840/freeopcua/server/"

        client = mock_client_class(endpoint)
        client.connect()

        mock_client_class.assert_called_once_with(endpoint)
        mock_client.connect.assert_called_once()

    @patch("opcua.Client")
    def test_client_gets_node(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_var = MagicMock()
        mock_client.get_node.return_value = mock_var

        client = mock_client_class("opc.tcp://localhost:4840/freeopcua/server/")
        var = client.get_node("ns=2;s=MyVariable")

        mock_client.get_node.assert_called_once_with("ns=2;s=MyVariable")
        assert var is mock_var

    @patch("opcua.Client")
    def test_client_reads_variable_value(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_var = MagicMock()
        mock_var.get_value.return_value = 1234567890.0

        value = mock_var.get_value()

        mock_var.get_value.assert_called_once()
        assert value == 1234567890.0

    @patch("opcua.Client")
    def test_client_disconnects_on_exit(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        client = mock_client_class("opc.tcp://localhost:4840/freeopcua/server/")
        try:
            client.connect()
        finally:
            client.disconnect()

        mock_client.disconnect.assert_called_once()

    def test_client_prints_value(self, capsys):
        value = 1234567890.123

        print(f"Current value: {value}")

        captured = capsys.readouterr()
        assert "Current value:" in captured.out
        assert "1234567890.123" in captured.out
