import json
import os
from dotenv import load_dotenv

load_dotenv()

def read_metadata(file_path):
    with open(file_path, 'r') as file:
        metadata = json.load(file)
    return metadata

metadata_path = os.getenv("METADATA_PATH")

metadata = read_metadata(metadata_path)

