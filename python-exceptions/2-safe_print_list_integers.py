#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To track the number of integers printed
    for i in range(x):  # Loop over the first 'x' elements
        try:
            print("{:d}".format(my_list[i]), end="")  # Print integer elements
            count += 1  # Increment count if integer is printed
        except (ValueError, TypeError):  # Skip non-integer elements
            continue
        except IndexError:  # Handle case where 'x' exceeds list length
            break
    print()  # Newline after printing all valid integers
    return count  # Return the number of integers printed
