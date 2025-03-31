"""
This is a solution for the wc-tool project.
"""
import argparse
import os


def get_file_path(input_file: str) -> str:
    """
    Get the absolute path of a file.
    """
    try:
        current_dir = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(current_dir, "..", input_file))
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return None


def get_file_size_in_bytes(file_path: str) -> int:
    """
    Get the size of a file in bytes.
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def get_file_lines(file_path: str) -> int:
    """
    Get the number of lines in a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as fp:
            lines = len(fp.readlines())
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def main():
    """
    Main function to parse command line arguments and
    call the appropriate functions.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", type=str,
                        help="the number of bytes in the file")
    parser.add_argument("-l", type=str,
                        help="the number of lines in the file")
    args = parser.parse_args()

    file_arg = args.c or args.l
    if not file_arg:
        parser.print_help()
        return

    file_path = get_file_path(file_arg)
    if not file_path:
        return

    match args:
        case _ if args.c:
            result = get_file_size_in_bytes(file_path)
            print(result)
        case _ if args.l:
            result = get_file_lines(file_path)
            print(result)


if __name__ == "__main__":
    main()
