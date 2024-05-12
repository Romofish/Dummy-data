# data_generator.py
import pandas as pd
import numpy as np
import random
import datetime
import logging
from iso3166 import countries

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_dummy_data(metadata, num_rows):
    datasets = {}

    # Iterate over each dataset in the metadata
    for dataset_name, variables in metadata["data"].items():
        data_frame = pd.DataFrame()
        labels_frame = pd.DataFrame(index=[0])

        # Iterate over each variable and its attributes within the dataset
        for var_name, attrs in variables.items():
            # Save variable labels
            labels_frame[var_name] = attrs.get("Variable Label", "No Label")

            # Handle controlled terms if they exist and are not empty
            controlled_terms = attrs.get("Controlled Terms, Codelist or Format", [])
            if controlled_terms and controlled_terms != [""]:
                if "ISO 8601 datetime or interval" in controlled_terms:
                    data_frame[var_name] = [datetime.datetime.now().isoformat() for _ in range(num_rows)]
                    # logging.info(f"Generated ISO 8601 datetime for {var_name}")
                elif var_name == "COUNTRY":
                    data_frame[var_name] = [random.choice(list(countries)).alpha3 for _ in range(num_rows)]
                    # logging.info(f"Generated country codes for {var_name}")
                else:
                    data_frame[var_name] = [random.choice(controlled_terms) for _ in range(num_rows)]
                    # logging.info(f"Generated controlled term data for {var_name}")
            else:
                # Fallback to Type if no valid controlled terms are provided
                if attrs.get("Type") == "Char":
                    data_frame[var_name] = ["NA" for _ in range(num_rows)]
                    # logging.info(f"Generated default Char data for {var_name}")
                elif attrs.get("Type") == "Num":
                    data_frame[var_name] = ["." for _ in range(num_rows)]
                    # logging.info(f"Generated default Num data for {var_name}")
                else:
                    logging.warning(f"No controlled terms or type information available for {var_name}")

        # Combine labels frame with data frame
        combined_frame = pd.concat([labels_frame, data_frame], ignore_index=True)
        datasets[dataset_name] = combined_frame

    return datasets

# # output_modifier.py to add logic for the NA/./Special values like MedDRA
# def modify_output(data_frame, additional_metadata):
#     for column in data_frame.columns:
#         if column in additional_metadata:
#             rules = additional_metadata[column]
#             # Apply specific rules, e.g., replacing values
#             data_frame[column] = data_frame[column].replace(rules['replace_if'], rules['replace_with'])
#     return data_frame

