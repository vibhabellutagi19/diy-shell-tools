import unittest

from src.main.tools.ccgrep.search import GrepSearch


# todo:
# 1.
class TestGrep(unittest.TestCase):
    def test_grep_with_empty_expression(self):
        """Test grep with empty expression."""
        test_input_text = ["This is a test"]
        grep_search = GrepSearch()
        results = grep_search.search_text("", test_input_text)
        self.assertEqual(results, test_input_text)

    def test_grep_search_one_letter_pattern_not_found(self):
        """Test grep search with one letter pattern not found."""
        test_input_text = """
            Judas Priest
            AC/DC
            Black Sabbath
            Aerosmith
            Iron Maiden
            Van Halen
            Mr. Big
            Guns N’ Roses
            Kiss
            Kinder Jungle
            Junkyard
        """
        test_input_text = test_input_text.strip().split("\n")
        grep_search = GrepSearch()
        results = grep_search.search_text("J", test_input_text)
        self.assertEqual(results, ["Judas Priest", "Kinder Jungle", "Junkyard"])

    def test_grep_search_digits(self):
        test_input_text = """
            Debbie just hit the wall, she never had it all
            One Prozac a day, husband's a CPA
            Her dreams went out the door when she turned 24

            Since Bruce Springsteen, Madonna, way before Nirvana
            There was U2 and Blondie, and music still on MTV
            Her two kids in high school, they tell her that she's uncool
            'Cause she's still preoccupied with 19, 19, 1985, 1985
        """
        test_input_text = test_input_text.strip().split("\n")
        grep_search = GrepSearch()
        results = grep_search.search_text(r"\d", test_input_text)
        expected_results = [
            "Her dreams went out the door when she turned 24",
            "There was U2 and Blondie, and music still on MTV",
            "'Cause she's still preoccupied with 19, 19, 1985, 1985",
        ]
        self.assertEqual(results, expected_results)

    def test_grep_search_words(self):
        test_input_text = """
            !
            @
            £
            $
            %
            ^
            &
            *
            (
            )
            pound
            dollar"""
        test_input_text = test_input_text.strip().split("\n")
        grep_search = GrepSearch()
        results = grep_search.search_text(r"\w", test_input_text)
        expected_results = ["pound", "dollar"]
        self.assertEqual(results, expected_results)

    def test_grep_search_words_begining_text(self):
        test_input_text = """
            Judas Priest
            AC/DC
            Black Sabbath
            Aerosmith
            Iron Maiden
            Motorhead
            Def Leppard
            Bon Jovi
            Y&T
            Damn Yankees
            Accept
            UFO
            Extreme
            April Wine
            Autograph"""
        test_input_text = test_input_text.strip().split("\n")
        grep_search = GrepSearch()
        results = grep_search.search_text("^A", test_input_text)
        expected_results = ["AC/DC", "Aerosmith", "Accept", "April Wine", "Autograph"]
        self.assertEqual(results, expected_results)

    def test_grep_search_words_ending_text(self):
        test_input_text = """
            Judas Priest
            AC/DC
            Black Sabbath
            Aerosmith
            Iron Maiden
            Motorhead
            Def Leppard
            Bon
            Y&T
            Damn Yankees
            Accept
            UFO
            Extreme
            April Wine
            Autograph"""
        test_input_text = test_input_text.strip().split("\n")
        grep_search = GrepSearch()
        results = grep_search.search_text("n$", test_input_text)
        expected_results = ["Iron Maiden", "Bon"]
        self.assertEqual(results, expected_results)
