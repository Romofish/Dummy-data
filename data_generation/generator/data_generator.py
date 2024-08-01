import pandas as pd
import numpy as np
import random
import datetime
import logging
import json
from iso3166 import countries

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to generate random value from range
def generate_random_from_range(ranges):
    selected_range = random.choice(ranges)
    return random.randint(selected_range["start"], selected_range["end"])

# Function to generate USUBJID
def generate_usubjid(studyid, subjid):
    return f"{studyid}{subjid}"

# Function to read general settings
def read_general_settings():
    GENERAL_SETTINGS_FILE_PATH = 'metadata/general_settings.json'
    if not os.path.exists(GENERAL_SETTINGS_FILE_PATH):
        return {}
    with open(GENERAL_SETTINGS_FILE_PATH, 'r') as f:
        settings = json.load(f)
    return settings

def generate_dummy_data(metadata, num_rows):
    datasets = {}
    general_settings = read_general_settings()

    # Pre-generate study-specific data
    studyid = general_settings["STUDYID"]["value"]
    siteid_ranges = general_settings["SITEID"]["ranges"]
    subjid_ranges = general_settings["SUBJID"]["ranges"]

    siteids = [generate_random_from_range(siteid_ranges) for _ in range(num_rows)]
    subjid_numbers = [generate_random_from_range(subjid_ranges) for _ in range(num_rows)]
    usubjids = [generate_usubjid(studyid, subjid) for subjid in subjid_numbers]

    # Iterate over each dataset in the metadata
    for dataset_name, variables in metadata["data"].items():
        data_frame = pd.DataFrame()
        labels_frame = pd.DataFrame(index=[0])

        # Iterate over each variable and its attributes within the dataset
        for var_name, attrs in variables.items():
            # Save variable labels
            labels_frame[var_name] = attrs.get("Variable Label", "No Label")

            if var_name == "STUDYID":
                data_frame[var_name] = [studyid for _ in range(num_rows)]
            elif var_name == "SITEID":
                data_frame[var_name] = siteids
            elif var_name == "SUBJID":
                data_frame[var_name] = subjid_numbers
            elif var_name == "USUBJID":
                data_frame[var_name] = usubjids
            else:
                # Handle controlled terms if they exist and are not empty
                controlled_terms = attrs.get("Controlled Terms, Codelist or Format", [])
                if controlled_terms and controlled_terms != [""]:
                    if "ISO 8601 datetime or interval" in controlled_terms:
                        data_frame[var_name] = [datetime.datetime.now().isoformat() for _ in range(num_rows)]
                        logging.info(f"Generated ISO 8601 datetime for {var_name}")
                    elif var_name == "COUNTRY":
                        data_frame[var_name] = [random.choice(list(countries)).alpha3 for _ in range(num_rows)]
                        logging.info(f"Generated country codes for {var_name}")
                    else:
                        data_frame[var_name] = [random.choice(controlled_terms) for _ in range(num_rows)]
                        logging.info(f"Generated controlled term data for {var_name}")
                else:
                    # Fallback to Type if no valid controlled terms are provided
                    if attrs.get("Type") == "Char":
                        data_frame[var_name] = ["NA" for _ in range(num_rows)]
                        logging.info(f"Generated default Char data for {var_name}")
                    elif attrs.get("Type") == "Num":
                        data_frame[var_name] = ["." for _ in range(num_rows)]
                        logging.info(f"Generated default Num data for {var_name}")
                    else:
                        logging.warning(f"No controlled terms or type information available for {var_name}")

        # Combine labels frame with data frame
        combined_frame = pd.concat([labels_frame, data_frame], ignore_index=True)
        datasets[dataset_name] = combined_frame

    return datasets
