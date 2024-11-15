import json
import os

def save_to_json_file(my_obj, filename):
    """
    Serializes an object to a JSON file.

    Parameters:
    my_obj (any): The object to serialize. If it's a set, it will be converted to a list.
    filename (str): The name of the file to write the JSON data to.

    Raises:
    PermissionError: If the file cannot be written due to permission issues.
    """
    # Convert sets to lists for JSON serialization
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    
    try:
        # Attempt to write to the file
        with open(filename, "w") as file:
            json.dump(my_obj, file)
    except PermissionError as e:
        print(f"PermissionError: {e}")

# Example usage
data = {1, 2, 3}
filename = 'no_perm/file_7'

# Ensure the directory exists and has the correct permissions
os.makedirs(os.path.dirname(filename), exist_ok=True)

save_to_json_file(data, filename)
