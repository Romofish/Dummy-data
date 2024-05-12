# main.py
from metadata_reader import load_metadata
from data_generator import generate_dummy_data
from dataset_selector import select_datasets
from output_manager import save_to_file
import os

# Load metadata
metadata = load_metadata()

# User's dataset selection and output path
user_selection = input("Enter dataset names separated by commas, or press enter to select all: ")
selected_datasets = [x.strip() for x in user_selection.split(',')] if user_selection else None

output_path = input("Enter the path where you want the datasets to be saved: ")

# Ensure output path is specified, provide default if empty
if not output_path:
    output_path = "backend/tests/outputs"  # Default path can be adjusted as needed

# Check if the output directory exists, if not, create it
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"Created output directory: {output_path}")

# Filter metadata based on selection
selected_metadata = select_datasets(metadata, selected_datasets)

# Generate data
num_rows = int(input("Enter the number of rows to generate: "))  
datasets = generate_dummy_data({"data": selected_metadata}, num_rows)

# Output to JSON and Excel and CSV
print("Available formats to save data: JSON, Excel, CSV")
format_input = input("Enter the formats separated by commas (e.g., json,excel) or type 'all' to save in all formats: ").lower()
if format_input == 'all':
    formats = ['json', 'excel', 'csv']
else:
    formats = format_input.split(',')

# format validation check
valid_formats = ['json', 'excel', 'csv']
formats = [format.strip() for format in formats if format.strip() in valid_formats]

# Output to selected formats
for name, data in datasets.items():
    save_to_file(data, name, output_path, formats)


