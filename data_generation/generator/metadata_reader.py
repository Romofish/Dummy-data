import json
import os
from dotenv import load_dotenv

load_dotenv()  

def load_metadata():
    """Load metadata from a JSON file specified in environment variables."""
    metadata_path = os.getenv("METADATA_PATH", "default_metadata.json")  # 提供一个默认路径作为后备
    try:
        with open(metadata_path, 'r') as file:
            metadata = json.load(file)
        return metadata
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {metadata_path} does not exist.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error decoding JSON from {metadata_path}")


def load_additional_metadata():
    """Load metadata from a JSON file specified in environment variables."""
    additional_metadata_path = os.getenv("ADDITIONAL_METADATA_PATH","default_addtional_metadata.json")
    try:
        with open(additional_metadata_path, 'r') as file:
            metadata = json.load(file)
        return metadata
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {additional_metadata_path} does not exist.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"Error decoding JSON from {additional_metadata_path}")
