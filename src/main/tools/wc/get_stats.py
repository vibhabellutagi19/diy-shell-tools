import os


class Stats:
    """Class for calculating stats for a input files"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_stats = os.stat(file_path)

    def count_bytes(self) -> int:
        """Count the number of bytes in a file"""
        return self.file_stats.st_size

    def count_lines(self):
        """count the number of lines in the file"""
        with open(self.file_path, 'r') as input_file:
            number_of_lines = len(input_file.readlines())
            return number_of_lines

        
