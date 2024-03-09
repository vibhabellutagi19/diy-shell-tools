from abc import ABC, abstractmethod


class BaseSource(ABC):
    @abstractmethod
    def get_data(self):
        """gets the data from the source"""
