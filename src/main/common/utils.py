"""Utility functions for the program"""


def display_results(result: list, input_file: str) -> None:
    """Display the results of the command
    :param result: The result of the command
    :param input_file: The input file"""
    for option in result:
        print(option, end=" ")
    print(f"{input_file.split('/')[-1]}")
