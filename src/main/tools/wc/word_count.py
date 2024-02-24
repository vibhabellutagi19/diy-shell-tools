import os
import sys
from dataclasses import dataclass
from typing import Union, Tuple, List

from base_commands.base_command import BaseCommand
from tools.wc.get_stats import Stats

OPTIONS_ERROR_MSG = "Invalid option(s) ['{}']. Valid options are: {}"


@dataclass
class ValidOptionsLabels:
    c: str = '-c'
    l: str = '-l'
    w: str = '-w'
    m: str = '-m'


class InvalidOptionError(Exception):
    pass


class WordCount(BaseCommand):
    def __init__(self, input_options):
        super().__init__(input_options)
        self.labels = ValidOptionsLabels()
        self.valid_options = [self.labels.c, self.labels.l, self.labels.w, self.labels.m]

    def validate_options(self):
        for option in self.options:
            if option not in self.valid_options:
                raise InvalidOptionError(OPTIONS_ERROR_MSG.format(option, ', '.join(self.valid_options)))

    def execute(self, file_path: str) -> Union[int, List]:
        """Execute the word count command on a file
        :param file_path: The path of the file to be processed
        """
        result = []
        try:
            self.validate_options()
            stats = Stats(file_path)
            if not self.options:
                count_bytes = stats.count_bytes()
                count_lines = stats.count_lines()
                count_words = stats.count_words()
                result = [count_bytes, count_lines, count_words]
            else:
                for option in self.options:
                    if option == self.labels.c:
                        count_bytes = stats.count_bytes()
                        result.append(count_bytes)
                    if option == self.labels.l:
                        count_lines = stats.count_lines()
                        result.append(count_lines)
                    if option == self.labels.w:
                        count_words = stats.count_words()
                        result.append(count_words)
                    if option == self.labels.m:
                        count_chars = stats.count_chars()
                        result.append(count_chars)
            return result

        except InvalidOptionError as e:
            print(e)
            sys.exit(1)


