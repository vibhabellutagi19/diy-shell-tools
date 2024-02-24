from abc import ABC, abstractmethod
from typing import Tuple, List, Union


class BaseCommand(ABC):

    def __init__(self, options: List[str] = None):
        self.options = options

    @abstractmethod
    def execute(self, file_path: str) -> Union[int, Tuple]:
        pass

    @abstractmethod
    def validate_options(self):
        pass
