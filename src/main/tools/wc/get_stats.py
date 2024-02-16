import os


class Stats:
    """Class for calculating stats for a input files"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_stats = os.stat(file_path)

    def count_bytes(self) -> int:
        """Count the number of bytes in a file"""
        return self.file_stats.st_size
        
