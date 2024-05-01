import pandas as pd
import json
import random
import os
from dotenv import load_dotenv
from datetime import datetime
from faker import Faker

load_dotenv()
fake = Faker()

# Load the variable and codelist metadata
variables_path = 'metadata/definitions/SDTMIG Metadata_metadata_variables.json'
codelists_path = 'metadata/SDTM Terminology-update_metadata_codelist.json'


# Define a function to generate random data based on the type
def generate_random_data_by_type(var_type, codelist):
    if var_type == 'Num':
        return random.randint(1, 100)
    elif var_type == 'Char':
        return fake.word()
    elif var_type == 'ISO 8601 datetime or interval':
        return datetime.now().isoformat()
    elif var_type == 'COUNTRY':
        return fake.country_code(representation='alpha-3')
    else:
        return fake.word()  # Default dummy data for any other type

# Define a function to create dummy data for a domain
def create_dummy_data(domain, num_records, variables_metadata, codelists_metadata):
    domain_vars = variables_metadata.get(domain, {})
    dummy_data = {}

    for var_name, var_attr in domain_vars.items():
        var_type = var_attr.get('Type')
        codelist = var_attr.get('Controlled Terms, Codelist or Format', '').strip()
        dummy_data[var_name] = []

        for _ in range(num_records):
            # Check for special type 'COUNTRY' or ISO datetime before looking for codelists
            if 'COUNTRY' in var_name.upper() or 'datetime' in var_type.lower() or 'interval' in var_type.lower():
                value = generate_random_data_by_type(var_type, None)
            elif codelist and codelist in codelists_metadata:
                # If a codelist is defined and exists, choose a random term from the codelist
                value = random.choice(codelists_metadata[codelist])
            elif codelist and codelist not in codelists_metadata:
                # If a codelist is defined but does not exist, use a placeholder
                value = "受控术语缺失"
            else:
                # If there is no codelist, generate data based on the type
                value = generate_random_data_by_type(var_type, None)

            dummy_data[var_name].append(value)

    return pd.DataFrame(dummy_data)

# Load metadata from JSON files
variables_metadata = load_json_data(variables_path)
codelists_metadata = load_json_data(codelists_path)

# Generate dummy data for the AE domain
dummy_domain = 'AE'
num_records = 10
dummy_dataset = create_dummy_data(dummy_domain, num_records, variables_metadata, codelists_metadata)

# Convert the dictionary to a JSON string
dummy_json = json.dumps(dummy_dataset, indent=4, ensure_ascii=False)
print(dummy_json)
