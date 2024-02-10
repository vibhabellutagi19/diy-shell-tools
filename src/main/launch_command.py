import sys


def main():
    # Check for the lenght of arguments
    if len(sys.argv) < 3:
        print("Usage: python3 launch_command.py <operation> <args> <file_or_directory_path>")
        sys.exit(1)
    command = sys.argv[1]
    input_args = sys.argv[2]
    input_file_name = sys.argv[3]


if __name__ == "__main__":
    main()
