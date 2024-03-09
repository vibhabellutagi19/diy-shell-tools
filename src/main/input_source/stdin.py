from abc import abstractmethod
import sys
from src.main.input_source.base_source import BaseSource


class StdIn(BaseSource):

    @abstractmethod
    def get_data(self):
        return sys.stdin.readlines()
