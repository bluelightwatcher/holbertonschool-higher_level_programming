#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:  # Checking if the list is not empty
        for i in reversed(my_list):  # Loop through the list in reverse order
            print("{:d}".format(i))  # Using str.format() to print the integer
