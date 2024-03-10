import unittest
from unittest.mock import Mock
from src.main.base_commands.base_command import BaseCommand

from src.main.common.utils import get_command_instance, get_input_instance
from src.main.input_source.base_source import BaseSource


class TestUtils(unittest.TestCase):
    def test_command_instance(self):
        args = Mock()
        args.command = "ccwc"
        args.options = ["-c"]
        command_instance = get_command_instance(args)
        self.assertIsInstance(command_instance, BaseCommand)

    def test_input_instance(self):
        input_file = "tests/data/test_input.txt"
        input_instance = get_input_instance(input_file)
        self.assertIsInstance(input_instance, BaseSource)
