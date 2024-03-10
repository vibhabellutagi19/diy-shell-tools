import unittest
from unittest.mock import patch
from io import StringIO
from src.main.common.utils import VALID_COMMANDS, InvalidCommandError
from src.main.run_command import (
    check_file_exists,
    parse_arguments,
    print_error_and_exit,
    validate_command,
)
from tests import TEST_ROOT


class TestRunCommand(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.test_file = f"{TEST_ROOT}/resources/test.txt"

    def test_check_file_exists(self):
        """Test check_file_exists function"""
        self.assertEqual(self.test_file, check_file_exists(self.test_file))

    def test_check_file_exists_error(self):
        """Test check_file_exists function with error"""
        with self.assertRaises(FileNotFoundError) as context:
            check_file_exists("nonexistent.txt")
        self.assertEqual("File 'nonexistent.txt' not found", str(context.exception))

    def test_valid_command(self):
        """Test valid command"""
        expected_output = "ccwc"
        actual_output = validate_command("ccwc")
        self.assertEqual(expected_output, actual_output)

    def test_invalid_command(self):
        """Test invalid command"""
        with self.assertRaises(InvalidCommandError) as context:
            validate_command("invalid")
        self.assertEqual(
            "Invalid command 'invalid'. Valid commands are: ccwc",
            str(context.exception),
        )

    def test_print_error_and_exit(self):
        """Test print_error_and_exit function"""
        with patch("sys.stderr", new_callable=StringIO):
            with self.assertRaises(SystemExit) as context:
                print_error_and_exit("error")
            self.assertEqual(1, context.exception.code)

    def test_parse_arguments_valid(self):
        """Test parse_arguments function with valid arguments"""
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            with patch(
                "sys.argv",
                ["run_command.py", "ccwc", "--option1", "--option2", "input.txt"],
            ):
                args = parse_arguments()
                self.assertEqual(args.command, "ccwc")
                self.assertEqual(args.options, ["--option1", "--option2"])
                self.assertEqual(args.input_file, "input.txt")
                self.assertEqual(mock_stderr.getvalue(), "")

    def test_parse_arguments_no_args(self):
        """Test parse_arguments function with no arguments"""
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            with patch("sys.argv", ["run_command.py"]):
                with self.assertRaises(SystemExit) as context:
                    parse_arguments()
                self.assertEqual(context.exception.code, 1)
                self.assertIn("usage:", mock_stderr.getvalue())

    def test_parse_arguments_invalid_command(self):
        """Test parse_arguments function with invalid command"""
        expected_exception = f"Invalid command 'invalid'. Valid commands are: {', '.join(VALID_COMMANDS)}"
        with patch("sys.stderr", new_callable=StringIO):
            with patch(
                "sys.argv",
                ["run_command.py", "invalid", f"{TEST_ROOT}/resources/test.txt"],
            ):
                with self.assertRaises(InvalidCommandError) as context:
                    parse_arguments()
                self.assertEqual(context.exception.args[0], expected_exception)

    def test_parse_arguments_missing_input_file(self):
        """Test parse_arguments function with missing input file"""
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            with patch("sys.argv", ["run_command.py", "ccwc", "-option1", "-option2"]):
                args = parse_arguments()
                self.assertEqual(args.command, "ccwc")
                self.assertEqual(args.options, ["-option1", "-option2"])
                self.assertIsNone(args.input_file)
                self.assertEqual(mock_stderr.getvalue(), "")
