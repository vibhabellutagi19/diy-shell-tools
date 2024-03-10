import unittest

from src.main.base_commands.command_factory import CommandsFactory
from src.main.input_source.base_source import BaseSource
from src.main.input_source.input_source_factory import InputSourceFactory
from src.main.tools.ccwc.word_count import InvalidOptionError
from tests import TEST_ROOT


class TestWordCount(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.test_file: str = f"{TEST_ROOT}/resources/test.txt"
        self.test_file_source: BaseSource = InputSourceFactory.create_source_instance(
            "file", self.test_file
        )
        self.test_stdin_source = InputSourceFactory.create_source_instance("stdin")

    def test_valid_options(self):
        """Test valid options for the ccwc command"""
        try:
            self.c_options = ["-c"]
            self.wc_instance = CommandsFactory.create_command_instance(
                "ccwc", self.c_options
            )
            self.wc_instance.validate_options()
        except InvalidOptionError as e:
            self.fail(f"Unexpected exception: {e}")

    def test_invalid_options(self):
        """Test invalid options for the ccwc command"""
        self.invalid_options = ["-a"]
        self.invalid_wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.invalid_options
        )

        with self.assertRaises(InvalidOptionError) as context:
            self.invalid_wc_instance.validate_options()
        expection_message = f"Invalid option(s) {self.invalid_options}. Valid options are: -c, -l, -w, -m"
        self.assertEqual(expection_message, str(context.exception))

    def test_invalid_option_error_from_execute(self):
        self.invalid_options = ["-a"]
        self.invalid_wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.invalid_options
        )

        with self.assertRaises(InvalidOptionError) as context:
            self.invalid_wc_instance.options = self.invalid_options
            self.invalid_wc_instance.execute(self.test_file)
        expection_message = f"Invalid option(s) {self.invalid_options}. Valid options are: -c, -l, -w, -m"
        self.assertEqual(expection_message, str(context.exception))

    def test_options_c_from_file(self):
        """Test the -c option: number of bytes in a file"""
        self.c_options = ["-c"]
        self.wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.c_options
        )
        expected_output = 335095
        actual_output = self.wc_instance.execute(self.test_file_source)
        self.assertEqual(expected_output, actual_output[0])

    def test_options_l_from_file(self):
        """Test the -l option: number of lines in a file"""
        self.options_l = ["-l"]
        self.wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.options_l
        )
        expected_output = 7145
        actual_output = self.wc_instance.execute(self.test_file_source)[0]
        self.assertEqual(expected_output, actual_output)

    def test_options_w_from_file(self):
        """Test the -w option: number of words in a file"""
        self.options_l = ["-w"]
        self.wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.options_l
        )
        expected_output = 58164
        actual_output = self.wc_instance.execute(self.test_file_source)[0]
        self.assertEqual(expected_output, actual_output)

    def test_options_m_with_file(self):
        """Test the -m option: number of characters in a file"""
        self.options_m = ["-m"]
        self.wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.options_m
        )
        expected_output = 332197
        actual_output = self.wc_instance.execute(self.test_file_source)[0]
        self.assertEqual(expected_output, actual_output)

    def test_for_default_options(self):
        """Test for no options: no options are provided, which is the equivalent to the -c, -l and -w options"""
        self.default_options = []
        self.wc_instance = CommandsFactory.create_command_instance(
            "ccwc", self.default_options
        )
        expected_output = [335095, 7145, 58164]
        actual_output = self.wc_instance.execute(self.test_file_source)
        self.assertEqual(expected_output, actual_output)
