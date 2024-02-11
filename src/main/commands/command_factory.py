from commands.word_count import WordCount


class CommandsFactory:
    command_classes = {
        'wc': WordCount,
    }

    @staticmethod
    def create_command_instance(command):
        """
        Creates command instance
        :param command:
        :return:
        """
        command_class = CommandsFactory.command_classes.get(command)
        if command_class:
            return command_class()
        else:
            raise ValueError("Invalid command name..")

