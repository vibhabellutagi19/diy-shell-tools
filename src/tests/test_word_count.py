import unittest

from base_commands.command_factory import CommandsFactory
from tools.wc.word_count import InvalidOptionError


class TestWordCount(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.valid_options = ['-c']
        self.invalid_options = ['-a']
        self.invalid_wc_instance = CommandsFactory.create_command_instance('wc', self.invalid_options)
        self.wc_instance = CommandsFactory.create_command_instance('wc', self.valid_options)

    def test_valid_options(self):
        """Test valid options for the wc command"""

        try:
            self.wc_instance.validate_options()
        except Exception as e:
            self.fail(f"Unexpected exception: {e}")
        else:
            self.assertTrue(True, "No exception raised for valid options")

    def test_invalid_options(self):
        """Test invalid options for the wc command"""
        with self.assertRaises(InvalidOptionError) as context:
            self.invalid_wc_instance.validate_options()
        expection_message = f"Invalid option(s) {self.invalid_options}. Valid options are: -c, -l, -w"
        self.assertEqual(expection_message, str(context.exception))

    def test_options_c(self):
        """Test the -c option: number of bytes in a file"""
        file_path = "resources/test.txt"
        expected_output = 335095
        actual_output = self.wc_instance.execute(file_path)
        self.assertEqual(expected_output, actual_output)

    def test_options_l(self):
        """Test the -l option: number of lines in a file"""

    def test_options_w(self):
        """Test the -w option: number of words in a file"""

    def test_for_default_options(self):
        """Test for no options: no options are provided, which is the equivalent to the -c, -l and -w options """
