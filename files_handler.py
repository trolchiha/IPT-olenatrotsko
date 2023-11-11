def save_to_file(file_name, text):
    try:
        with open(file_name, "w") as file:
            file.write(text)
        print(f"The result was saved to {file_name}")
    except Exception as e:
        print(f"Error writing to {file_name}: {e}")

def read_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"Error reading from {file_name}: {e}")
