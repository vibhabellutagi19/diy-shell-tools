class CommandsFactory:
    commands_classes = {
    }

    @staticmethod
    def create_command_instance(command):
        command_class = CommandsFactory.commands_classes.get(command)
        if command_class:
            return command_class()
        else:
            raise ValueError("Invalid command name..")

