import unittest
from io import StringIO
from unittest.mock import patch

from src.main import run_command
from tests import TEST_ROOT


class TestLaunchCommand(unittest.TestCase):
    """Test cases for the run_command module."""

    @patch("sys.argv", ["run_command.py", "ccwc", f"{TEST_ROOT}/resources/test.txt"])
    def test_main_with_valid_arguments(self):
        """Test the main function with valid arguments."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            run_command.main()
            output = fake_out.getvalue().strip()
            expected_output = "335095 7145 58164 test.txt"
            self.assertEqual(output, expected_output)

    @patch("sys.argv", ["run_command.py"])
    def test_main_with_no_arguments(self):
        """Test the main function with no arguments."""
        with self.assertRaises(SystemExit) as cm:
            run_command.main()
        self.assertEqual(cm.exception.code, 2)

    @patch(
        "sys.argv",
        ["run_command.py", "test_command", f"{TEST_ROOT}/resources/test.txt"],
    )
    def test_main_with_invalid_command(self):
        """Test the main function with invalid command."""
        with self.assertRaises(run_command.InvalidCommandError) as cm:
            run_command.main()
        self.assertEqual(
            cm.exception.args[0],
            "Invalid command 'test_command'. Valid commands are: ccwc",
        )

    @patch("sys.argv", ["run_command.py", "ccwc", "non_existing_file.txt"])
    def test_main_with_non_existing_file(self):
        """Test the main function with non existing file."""
        with self.assertRaises(SystemExit) as cm:
            run_command.main()
        self.assertEqual(cm.exception.code, 1)
