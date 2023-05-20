import json
import os

def convert_json_file(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Change class names
    for obj in data['objects']:
        if 'class' in obj:
            if obj['class'] == 'vehicle':
                obj['class'] = 'car'
            elif obj['class'] == 'license plate':
                obj['class'] = 'number'

    return data

# Path to the folder containing JSON files
json_folder = '/path/to/json_folder'

# List of JSON files to combine
json_files = ['Pos_0.png.json', 'Pos_10010.png.json', 'Pos_10492.png.json']

# Combine JSON files into a single JSON object
combined_data = {
    'combined_objects': []
}

for json_file in json_files:
    json_file_path = os.path.join(json_folder, json_file)
    data = convert_json_file(json_file_path)
    combined_data['combined_objects'].extend(data['objects'])

# Save the combined JSON file
output_file_path = os.path.join(json_folder, 'combined_output.json')
with open(output_file_path, 'w') as f:
    json.dump(combined_data, f)

print(f"Combined JSON files into {output_file_path}")