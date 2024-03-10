"""
main module to run the command line dyi-shell-tool
"""

import argparse
import sys

from src.main.common.utils import (
    check_file_exists,
    create_command_instance,
    create_input_instance,
    display_results,
    validate_command,
)


def print_error_and_exit(error_msg: str) -> None:
    """Print an error message and exit the program with a status of 1.
    :param error_msg: The error message to print
    """
    print("Usage: python run_command.py <command> <options> <input_file>")
    print("Error: %s", error_msg, file=sys.stderr)
    sys.exit(1)


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments and return the parsed arguments."""
    parser = argparse.ArgumentParser(
        usage="python run_command.py <command> [<options>] [<input_file>]"
    )
    parser.add_argument("command", type=str, help="Command to execute (ccwc)")
    parser.add_argument("options", nargs="*", help="Options for ccwc command")
    parser.add_argument("input_file", nargs="?", help="Input file path")

    try:
        args, unknown = parser.parse_known_args()
        options = []
        input_file = None
        for arg in args.options + unknown:
            if arg.startswith("-"):
                options.append(arg)
            else:
                input_file = arg
                break
    except SystemExit as e:
        print_error_and_exit(e)

    args.options = options
    args.input_file = input_file

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return args


def main():
    """Main function to run the dyi-shell-tool.
    Parses the command line arguments and runs the command."""
    args = parse_arguments()

    print(args)

    # validate the command and input file

    validate_command(args.command)
    if args.input_file:
        check_file_exists(args.input_file)

    # create instances
    command_instance = create_command_instance(args)
    input_instance = create_input_instance(args, args.input_file)
    result = command_instance.execute(input_instance)
    display_results(result, args.input_file)


if __name__ == "__main__":
    main()
