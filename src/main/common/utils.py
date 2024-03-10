"""Utility functions for the program"""

import os
from typing import Any
from src.main.base_commands.command_factory import CommandsFactory
from src.main.input_source.input_source_factory import InputSourceFactory


VALID_COMMANDS: list[str] = ["ccwc"]


class InvalidCommandError(Exception):
    """Exception raised for invalid commands"""


def display_results(result: list, file_path: str) -> None:
    """Display the results of the command
    :param result: The result of the command
    :param file_path: The input file"""

    for option in result:
        print(option, end=" ")
    if file_path:
        file_name = file_path.split("/")[-1]
        print(f"{file_name}")


def check_file_exists(file_path: str) -> str:
    """Check if the file exists. If not, raise a FileNotFoundError.
    :param file_path: The file path to check
    :return: The file path if it exists
    :raises FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")
    return file_path


def validate_command(command: Any) -> str:
    """Validate the command is one of the valid base_commands. If not, raise an InvalidCommandError.
    :param command: The command to validate
    :return: The command if it is valid
    :raises InvalidCommandError: If the command is not valid
    """
    if command not in VALID_COMMANDS:
        raise InvalidCommandError(
            f"Invalid command '{command}'. Valid commands are: {', '.join(VALID_COMMANDS)}"
        )
    return command


def get_command_instance(args):
    """Create an instance of the command based on the parsed arguments."""
    return CommandsFactory.create_command_instance(args.command, args.options)


def get_input_instance(input_file: str = None):
    """Create an instance of the input source based on the parsed arguments."""
    source_type = "file" if input_file else "stdin"
    return InputSourceFactory.create_source_instance(source_type, input_file)
