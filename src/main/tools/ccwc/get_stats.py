"""This module contains a class for calculating stats for a input files for the ccwc command"""

import os

from src.main.input_source.base_source import BaseSource


class Stats:
    """Class for calculating stats for a input files"""

    def __init__(self, input_source: BaseSource):
        self.file_stats = None
        self.file_path = input_source.path if hasattr(input_source, "path") else None
        self.contents: list = input_source.get_data()

    def count_bytes(self) -> int:
        """Count the number of bytes"""
        if self.file_path:
            self.file_stats = os.stat(self.file_path).size
        else:
            self.file_stats = len(self.contents)
        return self.file_stats

    def count_lines(self):
        """count the number of lines"""
        number_of_lines = len(self.contents)
        return number_of_lines

    def count_words(self):
        """count the number of words"""
        words = [word for word in self.contents if word]
        return len(words)

    def count_chars(self):
        """count the number of characters"""
        num_chars = sum(len(line) for line in self.contents)
        return num_chars
