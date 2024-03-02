""" This module contains the BaseCommand class,
which is an abstract class that defines the interface for all the"""
from abc import ABC, abstractmethod
from typing import Tuple, List, Union


class BaseCommand(ABC):
    """Base class for all commands"""

    def __init__(self, options: List[str] = None):
        self.options = options

    @abstractmethod
    def execute(self, file_path: str) -> Union[int, Tuple]:
        """Abstract method to execute the command"""

    @abstractmethod
    def validate_options(self):
        """Abstract method to validate the options"""
