from typing import Any
from src.main.input_source.base_source import BaseSource
from src.main.input_source.file import FileSource
from src.main.input_source.stdin import StdIn


class InputSourceFactory:  # pylint: disable=too-few-public-methods
    """Class to create source instances"""

    sources = {"file": FileSource, "stdin": StdIn}

    @staticmethod
    def create_source_instance(source: Any, path: str = None) -> BaseSource:
        """
        Creates source instance
        :param source: The source to get the data from
        :param path: The path to the file
        :return:
        """
        source_class = InputSourceFactory.sources.get(source)
        return source_class(path) if path else source_class()
