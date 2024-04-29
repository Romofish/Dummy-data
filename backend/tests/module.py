import pandas as pd
import json
import random
from datetime import datetime, timedelta

# ISO 8601日期生成函数
def generate_iso8601_datetime():
    current_time = datetime.now()
    random_date = current_time + timedelta(days=random.randint(-365, 365))
    return random_date.isoformat()

# 随机国家代码生成函数
def generate_country_code():
    country_codes = ['USA', 'CAN', 'GBR', 'AUS', 'DEU', 'FRA', 'JPN', 'CHN', 'IND', 'BRA']
    return random.choice(country_codes)

def load_json_data(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)['data']

def generate_dummy_value(var_name, var_details, codelist_values):
    if var_details['Type'] == 'Num':
        return random.randint(1, 1000)
    elif var_details['Type'] == 'Char':
        if codelist_values:
            return random.choice(codelist_values)
        elif var_details['Controlled Terms, Codelist or Format']:
            return "Missing in codelist"
        elif var_name == 'COUNTRY':
            return generate_country_code()
        else:
            return "DUMMY"
    elif var_details['Type'] == 'ISO 8601 datetime or interval':
        return generate_iso8601_datetime()
    else:
        return "N/A"

def generate_dummy_dataset(domain, num_rows, variables_metadata, codelists_metadata):
    variables = variables_metadata.get(domain, {})
    dummy_dataset = {var_name: [] for var_name in variables}

    for _ in range(num_rows):
        for var_name, var_details in variables.items():
            codelist_key = var_details.get('Controlled Terms, Codelist or Format')
            codelist_values = codelists_metadata.get(codelist_key, [])
            dummy_value = generate_dummy_value(var_name, var_details, codelist_values)
            dummy_dataset[var_name].append(dummy_value)

    return pd.DataFrame(dummy_dataset)

# 加载 JSON 数据
variables_json_path = 'metadata/definitions/SDTMIG Metadata_metadata_variables.json' 
codelists_json_path = 'metadata/SDTM Terminology-update_metadata_codelist.json'  
variables_metadata = load_json_data(variables_json_path)
codelists_metadata = load_json_data(codelists_json_path)

# 生成虚拟数据集
domain_to_generate = 'DM'
num_rows_to_generate = 10
dummy_dataset = generate_dummy_dataset(domain_to_generate, num_rows_to_generate, variables_metadata, codelists_metadata)

# 打印或保存虚拟数据集
print(dummy_dataset)
dummy_dataset.to_csv('backend/tests/outputs/dummy_dataset.csv', index=False)

