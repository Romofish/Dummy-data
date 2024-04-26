import pandas as pd
import json
from datetime import datetime

def extract_codelist_to_json(excel_path, output_json_path):
    # Load the Excel sheet
    sheet_name = 'SDTM Terminology 2024-03-29'
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Organizing data hierarchically
    hierarchical_data = {}
    for _, row in df.dropna(subset=['Codelist Name', 'Codelist()', 'CDISC Submission Value']).iterrows():
        codelist_name = row['Codelist Name']
        codelist = row['Codelist()']
        cdisc_value = row['CDISC Submission Value']

        if codelist_name not in hierarchical_data:
            hierarchical_data[codelist_name] = {}
        
        if codelist not in hierarchical_data[codelist_name]:
            hierarchical_data[codelist_name][codelist] = []

        hierarchical_data[codelist_name][codelist].append(cdisc_value)

    # Adding a header with metadata
    metadata = {
        'source_file': excel_path.split('/')[-1],
        'extraction_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'version': '2024-03-29',
        'data': hierarchical_data
    }

    # Save to JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)

    print(f"Data extracted and saved to {output_json_path}")

# Example usage of the function
if __name__ == "__main__":
    excel_path = 'metadata/SDTM Terminology-update.xlsx'  # Modify with the path to your Excel file
    output_json_path = excel_path.replace('.xlsx', '_metadata_codelist.json')  # Saves JSON in the same location
    extract_codelist_to_json(excel_path, output_json_path)
