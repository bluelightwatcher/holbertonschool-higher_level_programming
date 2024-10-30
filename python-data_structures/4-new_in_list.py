#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Check if idx is out of bounds
        return my_list[:]  # Return a copy of the original list

    # Create a copy of the original list
    new_list = my_list[:]

    # Replace the element at the specified index
    new_list[idx] = element

    return new_list
