import sys
from src.main.input_source.base_source import BaseSource


class StdIn(BaseSource):

    def get_data(self) -> list[str]:
        contents: list[str] = sys.stdin.readlines()
        return contents
