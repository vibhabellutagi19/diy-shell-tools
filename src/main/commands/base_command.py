from abc import ABC, abstractmethod


class BaseCommand(ABC):
    def __init__(self, file_path: str):
        self.input_file_path = file_path

    @abstractmethod
    def execute(self):
        pass
