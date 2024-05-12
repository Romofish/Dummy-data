# extract_addtional_metadata.py
import json

def load_metadata(file_path):
    """Load metadata from a JSON file."""
    with open(file_path, 'r') as file:
        metadata = json.load(file)
    return metadata

def extract_clarification_needed(metadata):
    """Extract variables that need further clarification based on Controlled Terms, Codelist, or Format."""
    clarification_needed = {}

    # Assuming metadata is structured with datasets under a 'data' key
    for dataset_name, variables in metadata['data'].items():
        # Each dataset might need its own list of variables needing clarification
        clarification_needed[dataset_name] = []
        for var_name, attrs in variables.items():
            controlled_terms = attrs.get("Controlled Terms, Codelist or Format", [])
            # Check if controlled terms is empty or contains an empty string or 'MedDRA'
            if not controlled_terms or "" in controlled_terms or "MedDRA" in controlled_terms:
                clarification_needed[dataset_name].append(var_name)

    return clarification_needed

# Usage
metadata_path = 'metadata/default_metadata.json'
metadata = load_metadata(metadata_path)
variables_needing_clarification = extract_clarification_needed(metadata)

# Optionally, save the results to a JSON file for further processing
output_path = 'metadata/vars_need_clar.json'
with open(output_path, 'w') as f:
    json.dump(variables_needing_clarification, f, indent=4)

print(f"Variables needing clarification have been extracted and saved to {output_path}.")
