"""This module contains a class for calculating stats for a input files for the ccwc command"""

import os

from src.main.input_source.base_source import BaseSource


class Stats:
    """Class for calculating stats for a input files"""

    def __init__(self, input_source: BaseSource) -> None:
        self.file_stats = None
        self.file_path = input_source.path if hasattr(input_source, "path") else None
        self.contents: list = input_source.get_data()

    def count_bytes(self) -> int:
        """Count the number of bytes"""
        if self.file_path:
            self.file_stats = os.stat(self.file_path).st_size
        else:
            self.file_stats = len(self.contents)
        return self.file_stats

    def count_lines(self) -> int:
        """count the number of lines"""
        number_of_lines: int = len(self.contents)
        return number_of_lines

    def count_words(self) -> int:
        """count the number of words"""
        words = [word for line in self.contents for word in line.split()]
        num_of_words = len(words)
        return num_of_words

    def count_chars(self) -> int:
        """count the number of characters with whitespaces"""
        num_chars = sum(len(line) for line in self.contents)
        return num_chars
