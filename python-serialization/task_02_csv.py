import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to a JSON file.

    Parameters:
    csv_filename (str): The name of the CSV file to be converted.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file for reading
        with open(csv_filename, 'r') as csv_file:
            # Use DictReader to convert each row to a dictionary
            csv_reader = csv.DictReader(csv_file)

            # Convert the rows to a list of dictionaries
            data = [row for row in csv_reader]

        # Serialize the data and write to 'data.json'
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data from {csv_filename} has been successfully converted to 'data.json'.")
        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
