import json

def save_data(filename, data):
    with open(filename, 'w') as file:
        workout_data = [item.to_dict() for item in data]
        json.dump(workout_data, file, indent=4)

def load_data(file_path, object_class):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return [object_class.from_dict(item) for item in data]
            else:
                raise ValueError("Expected a list of dictionaries in the JSON file.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except ValueError:
        return []