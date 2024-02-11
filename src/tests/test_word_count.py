import unittest

from commands.command_factory import CommandsFactory


class TestWordCount(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.options = '-c'
        self.wc_instance = CommandsFactory.create_command_instance('wc', self.options)

    def test_valid_options(self):
        """Test valid options for the wc command"""

    def test_invalid_options(self):
        """Test invalid options for the wc command"""

    def test_options_c(self):
        """Test the -c option: number of bytes in a file"""

    def test_options_l(self):
        """Test the -l option: number of lines in a file"""

    def test_options_w(self):
        """Test the -w option: number of words in a file"""

    def test_for_default_options(self):
        """Test for no options: no options are provided, which is the equivalent to the -c, -l and -w options """

