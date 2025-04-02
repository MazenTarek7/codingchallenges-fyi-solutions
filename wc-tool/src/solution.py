"""
This is a solution for the wc-tool project.
"""
import argparse
import os
import sys


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


def get_file_words(file_path: str) -> int:
    """
    Get the number of words in a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as fp:
            content = fp.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def get_file_characters(file_path: str) -> int:
    """
    Get the number of characters in a file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as fp:
            content = fp.read()
            char_count = len(content)
            return char_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def main():
    """
    Main function to parse command line arguments and
    call the appropriate functions.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", action="store_true",
                        help="display the number of bytes in the file")
    parser.add_argument("-l", action="store_true",
                        help="display the number of lines in the file")
    parser.add_argument("-w", action="store_true",
                        help="display the number of words in the file")
    parser.add_argument("-m", action="store_true",
                        help="display the number of characters in the file")
    parser.add_argument("file", type=str, nargs="?",
                        help="the file to process")

    args = parser.parse_args()

    if not args.file:
        input_text = sys.stdin.read()
        size = len(input_text.encode('utf-8'))
        lines = len(input_text.splitlines())
        words = len(input_text.split())
        characters = len(input_text)

        if not (args.c or args.l or args.w or args.m):
            print(f"{lines} {words} {size}")
        else:
            if args.c:
                print(size)
            if args.l:
                print(lines)
            if args.w:
                print(words)
            if args.m:
                print(characters)
        return

    file_path = get_file_path(args.file)
    if not file_path:
        return

    if not (args.c or args.l or args.w or args.m):
        size = get_file_size_in_bytes(file_path)
        lines = get_file_lines(file_path)
        words = get_file_words(file_path)
        print(f"{lines} {words} {size} {args.file}")
    else:
        if args.c:
            print(get_file_size_in_bytes(file_path))
        if args.l:
            print(get_file_lines(file_path))
        if args.w:
            print(get_file_words(file_path))
        if args.m:
            print(get_file_characters(file_path))


if __name__ == "__main__":
    main()
