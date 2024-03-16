import unittest

from src.main.tools.ccgrep.search import GrepSearch


# todo:
# 1.
class TestGrep(unittest.TestCase):
    def test_grep_with_empty_expression(self):
        """Test grep with empty expression."""
        test_input_text = "This is a test"
        grep_search = GrepSearch()
        results = grep_search.search_text("", test_input_text)
        self.assertEqual(results, test_input_text)
