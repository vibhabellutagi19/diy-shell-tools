import unittest
from unittest.mock import patch
from src.main.common.utils import get_command_instance


class TestUtils(unittest.TestCase):
    @patch("src.main.common.utils.CommandsFactory.create_command_instance")
    def test_get_command_instance(self, mock_create_command_instance):
        """Test get_command_instance function"""
        args = MockArgs(command="ccwc", options=["--option1", "--option2"])
        get_command_instance(args)
        mock_create_command_instance.assert_called_once_with(
            "ccwc", ["--option1", "--option2"]
        )


class MockArgs:
    def __init__(self, command, options):
        self.command = command
        self.options = options


if __name__ == "__main__":
    unittest.main()
