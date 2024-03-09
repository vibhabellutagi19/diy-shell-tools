from abc import abstractmethod
from src.main.input_source.base_source import BaseSource


class FileSource(BaseSource):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def get_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
