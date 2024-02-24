import os
import re


class Stats:
    """Class for calculating stats for a input files"""

    def __init__(self, file_path: str):
        self.file_stats = None
        self.file_path = file_path
        
    def count_bytes(self) -> int:
        """Count the number of bytes in a file"""
        self.file_stats = os.stat(self.file_path)
        return self.file_stats.st_size

    def count_lines(self):
        """count the number of lines in the file"""
        with open(self.file_path, 'r') as input_file:
            number_of_lines = len(input_file.readlines())
            return number_of_lines

    def count_words(self):
        """count the number of words in the file"""
        with open(self.file_path, 'r') as input_file:
            content = input_file.read()
            words_and_space = re.split(r'\s+', content)
            words = [word for word in words_and_space if word]
            return len(words)

    def count_chars(self):
        """count the number of characters in the file"""
        with open(self.file_path, 'r') as input_file:
            content = input_file.read()
            return len(content)
            

        
