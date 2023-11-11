def save_to_file(file_name, text):
    '''
    Save text to a file.

    Parameters:
        file_name (str): The name of the file to save the text to.
        text (str): The text to be saved to the file.

    Returns:
        None

    Prints:
        str: A message indicating whether the save operation was successful or if there was an error.
    '''
    try:
        with open(file_name, "w") as file:
            file.write(text)
        print(f"The result was saved to {file_name}")
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def read_from_file(file_name):
    '''
    Read text from a file.

    Parameters:
        file_name (str): The name of the file to read text from.

    Returns:
        str: The content of the file.

    Prints:
        str: A message indicating whether the read operation was successful or if there was an error.
    '''
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
