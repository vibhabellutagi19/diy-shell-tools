from typing import Any
from src.main.input_source.base_source import BaseSource


class FileSource(BaseSource):
    def __init__(self, path) -> None:
        self.path: Any = path

    def get_data(self) -> list[str]:
        with open(self.path, "r", encoding="utf-8") as file:
            content: list[str] = file.readlines()
            return content
