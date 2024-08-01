import os
import json

CONFIG_FILE_PATH = 'metadata/default_metadata.json'
OUTPUT_FILE_PATH = 'backend/tests/outputs/interact/LB.json'
GENERAL_SETTINGS_FILE_PATH = 'metadata/general_settings.json'

def read_config():
    with open(CONFIG_FILE_PATH, 'r') as f:
        config = json.load(f)
    return config

def update_config(new_config):
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(new_config, f, indent=4)

def get_domain_config(domain):
    config = read_config()
    domain_config = config['data'].get(domain, {})
    return domain_config

def update_domain_variable_config(domain, variable, updated_config):
    config = read_config()
    if domain in config['data'] and variable in config['data'][domain]:
        config['data'][domain][variable] = updated_config
        update_config(config)
        return {"message": "Config updated successfully"}
    else:
        return {"error": "Domain or variable not found"}

def read_output():
    if not os.path.exists(OUTPUT_FILE_PATH):
        return {}
    with open(OUTPUT_FILE_PATH, 'r') as f:
        data = json.load(f)
    return data

def update_output(new_data):
    with open(OUTPUT_FILE_PATH, 'w') as f:
        json.dump(new_data, f, indent=4)

def get_processed_output():
    data = read_output()
    if isinstance(data, list) and len(data) > 0:
        descriptions = data[0]
        records = data[1:]
    else:
        descriptions = {}
        records = []
    return {"descriptions": descriptions, "records": records}

def read_general_settings():
    if not os.path.exists(GENERAL_SETTINGS_FILE_PATH):
        return {}
    with open(GENERAL_SETTINGS_FILE_PATH, 'r') as f:
        settings = json.load(f)
    return settings

def update_general_settings(new_settings):
    with open(GENERAL_SETTINGS_FILE_PATH, 'w') as f:
        json.dump(new_settings, f, indent=4)
