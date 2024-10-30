import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename where the XML will be saved.
    """
    # Create the root element 'data'
    root = ET.Element("data")

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        # Create a sub-element for each key-value pair
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert the value to string as XML stores text data

    # Create an ElementTree object with the root
    tree = ET.ElementTree(root)

    # Write the XML tree to the specified file
    with open(filename, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

    print(f"Dictionary serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The filename of the XML file to deserialize.

    Returns:
    dict: A dictionary representation of the XML data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Convert XML elements back to a dictionary
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text  # Use child.tag as key and child.text as value

        return result_dict

    except Exception as e:
        print(f"An error occurred while deserializing the XML file: {e}")
        return None
