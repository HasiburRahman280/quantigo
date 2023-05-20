import json
import os

def convert_json_file(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Determine the presence of categories (vehicle and license plate)
    vehicle_present = False
    license_plate_present = False

    if 'objects' in data:
        for obj in data['objects']:
            if 'class' in obj and obj['class'] == 'vehicle':
                vehicle_present = True
            elif 'class' in obj and obj['class'] == 'license plate':
                license_plate_present = True

    # Create the formatted JSON
    formatted_data = {
        'presence': {
            'vehicle': vehicle_present,
            'license plate': license_plate_present
        }
    }

    # Save the formatted JSON file
    output_file_path = 'formatted_' + os.path.basename(json_file_path)
    with open(output_file_path, 'w') as f:
        json.dump(formatted_data, f)

    print(f"Converted {json_file_path} to {output_file_path}")

# Path to the folder containing JSON files
json_folder = '/path/to/json_folder'

# List all JSON files in the folder
json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

# Process each JSON file
for json_file in json_files:
    json_file_path = os.path.join(json_folder, json_file)
    convert_json_file(json_file_path)