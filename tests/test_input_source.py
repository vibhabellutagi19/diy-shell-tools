from io import StringIO
import unittest
from unittest.mock import patch

from src.main.input_source.stdin import StdIn


class TestInputSource(unittest.TestCase):
    @patch("sys.stdin", StringIO("line1\nline2\nline3\n"))
    def test_get_data(self):
        stdin = StdIn()
        expected_output = ["line1\n", "line2\n", "line3\n"]
        actual_output = stdin.get_data()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdin", StringIO(""))
    def test_get_data_empty(self):
        stdin = StdIn()
        expected_output = []
        actual_output = stdin.get_data()
        self.assertEqual(expected_output, actual_output)
