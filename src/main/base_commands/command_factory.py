""" This module is responsible for creating command instances usinf factory pattern """

from typing import Any

from ..tools.ccwc.word_count import WordCount


class CommandsFactory:  # pylint: disable=too-few-public-methods
    """Class to create command instances"""

    command_classes = {
        "ccwc": WordCount,
    }

    @staticmethod
    def create_command_instance(command: Any, options: list[str]):
        """
        Creates command instance
        :param options:
        :param command:
        :return:
        """
        command_class = CommandsFactory.command_classes.get(command)
        return command_class(options)
