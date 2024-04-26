import json
import random
import configparser

def load_metadata(filename):
    with open(filename, 'r') as file:
        metadata = json.load(file)
    return metadata

def generate_dm_data(num_records, metadata):
    data = []
    sex_values = metadata['metadata'][1]['values']
    race_values = metadata['metadata'][3]['values']
    for i in range(num_records):
        # PENDING FOR EXTRACT TO MODULE FC 2024-04-26
        record = {
            'USUBJID': f'SUBJ00{i}',
            'SEX': random.choice(sex_values),
            'AGE': random.randint(18, 80),
            'RACE': random.choice(race_values)
        }
        data.append(record)
    return data

def generate_ae_data(num_records, metadata):
    # Similar logic as generate_dm_data for AE domain
    pass

def generate_cm_data(num_records, metadata):
    # Similar logic as generate_dm_data for CM domain
    pass

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    datasets = config['General']['datasets'].split(', ')
    num_records = int(config['General']['num_records'])
    metadata = load_metadata('metadata.json')

    for dataset in datasets:
        generate_func = globals()[f'generate_{dataset.lower()}_data']
        data = generate_func(num_records, metadata)
        save_data_to_file(data, f'{dataset.lower()}_data.json')

if __name__ == "__main__":
    main()
