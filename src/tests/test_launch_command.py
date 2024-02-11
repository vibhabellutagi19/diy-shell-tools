import unittest
from io import StringIO
from unittest.mock import patch

import launch_command


class TestLaunchCommand(unittest.TestCase):
    @patch('sys.argv', ['launch_command.py', 'wc', '-l', '-c', f'resources/test.txt'])
    def test_main_with_valid_arguments(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            launch_command.main()
            output = fake_out.getvalue().strip()
            expected_output = ""
            self.assertEqual(output, expected_output)

    @patch('sys.argv', ['launch_command.py'])
    def test_main_with_no_arguments(self):
        with self.assertRaises(SystemExit) as cm:
            launch_command.main()
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['launch_command.py', 'test_command', f'resources/test.txt'])
    def test_main_with_invalid_command(self):
        with self.assertRaises(SystemExit) as cm:
            launch_command.main()
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['launch_command.py', 'wc', 'non_existing_file.txt'])
    def test_main_with_non_existing_file(self):
        with self.assertRaises(SystemExit) as cm:
            launch_command.main()
        self.assertEqual(cm.exception.code, 1)
