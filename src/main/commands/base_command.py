from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @abstractmethod
    def execute(self, file_path: str):
        pass

    @abstractmethod
    def validate_options(self):
        pass
