from typing import List

from tools.wc.word_count import WordCount


class CommandsFactory:
    command_classes = {
        'ccwc': WordCount,
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
        return command_class(options)

