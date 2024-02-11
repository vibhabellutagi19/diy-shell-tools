from typing import List

from commands.word_count import WordCount


class CommandsFactory:
    command_classes = {
        'wc': WordCount,
    }

    @staticmethod
    def create_command_instance(command, options: List[str]):
        """
        Creates command instance
        :param options:
        :param command:
        :return:
        """
        command_class = CommandsFactory.command_classes.get(command)
        if command_class:
            return command_class(options)
        else:
            raise KeyError(f"Invalid command name: {command}")

