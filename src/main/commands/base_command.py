from abc import ABC, abstractmethod
from typing import Tuple, List


class BaseCommand(ABC):

    def __init__(self, options: List[str]):
        self.options = options

    @abstractmethod
    def execute(self, file_path: str):
        pass

    @abstractmethod
    def validate_options(self):
        pass
