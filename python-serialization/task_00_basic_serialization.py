import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The filename of the output JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # indent for pretty-printing
        print(f"Data serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file.

    Parameters:
    filename (str): The filename of the input JSON file.

    Returns:
    dict: The deserialized Python dictionary.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded and deserialized from '{filename}'.")
        return data
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None
