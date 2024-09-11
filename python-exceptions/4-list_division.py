#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # This will store the results of the divisions
    for i in range(list_length):  # Loop through the range of list_length
        try:
            # Attempt to divide elements from both lists
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")  # Handle division by zero
            result = 0  # Division result is 0 in case of division by 0
        except (TypeError, ValueError):
            print("wrong type")  # Handle cases where elements are not numbers
            result = 0  # Division result is 0 if the type is wrong
        except IndexError:
            print("out of range")  # Handle cases where one list is too short
            result = 0  # Division result is 0 if index is out of range
        finally:
            new_list.append(result)  
    return new_list  # Return the new list with all results
