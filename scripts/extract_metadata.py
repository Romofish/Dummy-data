# Extracts metadata from the 'Variables' sheet of the SDTMIG Metadata Excel file and saves it to a JSON file for merging with the codelist metadata.
import pandas as pd
import json
from datetime import datetime

def extract_variables_metadata(excel_path, output_json_path):
    # Load the Excel sheet
    sheet_name = 'Variables'
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Filter out 'Role' and 'CDISC Notes' columns
    relevant_columns = [col for col in df.columns if col not in ['Role', 'CDISC Notes']]

    # Initialize hierarchical data
    hierarchical_data = {}

    # Group by 'Domain' and iterate over each group
    for domain, group in df.groupby('Domain'):
        domain_metadata = {}

        # Iterate over each row in the group
        for _, row in group.iterrows():
            variable_name = row['Variable Name']  # Corrected column name
            # Exclude 'Domain' and 'Variable Name' columns from variable metadata
            variable_metadata = {col: row[col] for col in relevant_columns if col not in ['Domain', 'Variable Name']}
            domain_metadata[variable_name] = variable_metadata

        # Add domain metadata to hierarchical data
        hierarchical_data[domain] = domain_metadata

    # Adding a header with metadata
    metadata = {
        'source_file': excel_path.split('/')[-1],
        'extraction_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'version': 'SDTMIG 3.4',
        'data': hierarchical_data
    }

    # Save to JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

    print(f"Data extracted and saved to {output_json_path}")

# Example usage of the function
if __name__ == "__main__":
    excel_path = 'metadata/definitions/SDTMIG Metadata.xlsx'  # Replace with the path to your Excel file
    output_json_path = excel_path.replace('.xlsx', '_metadata_variables.json')  # Saves JSON in the same location
    extract_variables_metadata(excel_path, output_json_path)
