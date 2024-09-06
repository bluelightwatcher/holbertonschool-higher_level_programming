#!/usr/bin/python3
import sys


def main():
    # Retrieve arguments passed to script (ex script name)
    args = sys.argv[1:]

    # Convert all arguments to integers and compute their sum
    total = sum(int(arg) for arg in args)

    # Print the result followed by a newline
    print(total)


if __name__ == "__main__":
    main()
