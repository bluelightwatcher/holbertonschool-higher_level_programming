#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Set defaults for tuple_a and tuple_b in case they're smaller than 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Only take the first two elements and sum them up
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
