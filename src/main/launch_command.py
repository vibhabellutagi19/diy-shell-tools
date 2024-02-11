import os
import sys

import argparse

VALID_COMMANDS = ['wc']


class InvalidCommandError(Exception):
    pass

def check_file_exists(file_path: str) -> str:
    """Check if the file exists. If not, raise a FileNotFoundError.
    :param file_path: The file path to check
    :return: The file path if it exists
    :raises FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")
    return file_path


def validate_command(command) -> str:
    """Validate the command is one of the valid commands. If not, raise an InvalidCommandError.
    :param command: The command to validate
    :return: The command if it is valid
    :raises InvalidCommandError: If the command is not valid
    """
    if command not in VALID_COMMANDS:
        raise InvalidCommandError(f"Invalid command '{command}'. Valid commands are: {', '.join(VALID_COMMANDS)}")
    return command


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', metavar='command', type=str, help="Command to execute (e.g., wc)")
    parser.add_argument('options', metavar='options', type=str, nargs='*', help='Options for the command')
    parser.add_argument('input_file', metavar='file', type=str, help='Input file to process')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if len(sys.argv) < 2 or sys.argv[1] not in VALID_COMMANDS:
        try:
            validate_command(sys.argv[1])
        except InvalidCommandError as e:
            print(f"Usage: python launch_command.py <command> <options> <input_file>")
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if len(sys.argv) < 4 or sys.argv[-1] not in os.listdir():
        try:
            check_file_exists(sys.argv[-1])
        except FileNotFoundError as e:
            print(f"Usage: python launch_command.py <command> <options> <input_file>")
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
