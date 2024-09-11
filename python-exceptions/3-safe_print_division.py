#!/usr/bin/python3

def safe_print_division(a, b):
    result = None  # Initialize result to None
    try:
        result = a / b  # Attempt to divide a by b
    except ZeroDivisionError:  # Handle division by zero
        result = None  # Set result to None if division by zero occurs
    finally:
        print("Inside result: {}".format(result)) 
    return result
