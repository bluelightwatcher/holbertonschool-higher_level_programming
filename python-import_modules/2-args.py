#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]  # We skip the first argument (the script name)
    num_args = len(argv)

    # Handle no arguments case
    if num_args == 0:
        print("0 arguments.")
    else:
        # Handle single or multiple arguments
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")

        # Print each argument with its position
        for index, arg in enumerate(argv, start=1):
            print(f"{index}: {arg}")


# Ensure code is executed only when the script is run directly
if __name__ == "__main__":
    main()
