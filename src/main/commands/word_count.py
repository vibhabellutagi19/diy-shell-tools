from dataclasses import dataclass

from commands.base_command import BaseCommand

OPTIONS_ERROR_MSG = "Invalid option(s) ['{}']. Valid options are: {}"


@dataclass
class ValidOptionsLabels:
    c: str = '-c'
    l: str = '-l'
    w: str = '-w'


class InvalidOptionError(Exception):
    pass


class WordCount(BaseCommand):
    def __init__(self, options):
        super().__init__(options)
        self.labels = ValidOptionsLabels()
        self.valid_options = [self.labels.c, self.labels.l, self.labels.w]

    def validate_options(self):
        for option in self.options:
            if option not in self.valid_options:
                raise InvalidOptionError(OPTIONS_ERROR_MSG.format(option, ', '.join(self.valid_options)))

    def execute(self, file_path: str):
        pass
