# import json

# CONFIG_FILE_PATH = 'metadata/default_metadata.json'
# OUTPUT_FILE_PATH = 'backend/tests/outputs/interact/LB.json'  # test output file path

# def read_config():
#     with open(CONFIG_FILE_PATH, 'r') as f:
#         config = json.load(f)
#     return config

# def update_config(new_config):
#     with open(CONFIG_FILE_PATH, 'w') as f:
#         json.dump(new_config, f, indent=4)

# def get_domain_config(domain):
#     config = read_config()
#     domain_config = config['data'].get(domain, {})
#     return domain_config

# def update_domain_variable_config(domain, variable, updated_config):
#     config = read_config()
#     if domain in config['data'] and variable in config['data'][domain]:
#         config['data'][domain][variable] = updated_config
#         update_config(config)
#         return {"message": "Config updated successfully"}
#     else:
#         return {"error": "Domain or variable not found"}

# def read_json():
#     with open(OUTPUT_FILE_PATH, 'r') as f:
#         data = json.load(f)
#     return data

# def update_json(new_data):
#     with open(OUTPUT_FILE_PATH, 'w') as f:
#         json.dump(new_data, f, indent=4)

# def get_processed_output():
#     data = read_json()
#     config = read_config()
    
#     for domain, variables in data.items():
#         if domain in config['data']:
#             for variable, details in variables.items():
#                 if variable in config['data'][domain]:
#                     details['Controlled Terms, Codelist or Format'] = config['data'][domain][variable].get('Controlled Terms, Codelist or Format', [])
    
#     return data

import os
import json

# 文件路径
CONFIG_FILE_PATH = 'metadata/default_metadata.json'
OUTPUT_FILE_PATH = 'backend/tests/outputs/interact/LB.json'  # test output file path

# 读取元数据配置文件
def read_config():
    with open(CONFIG_FILE_PATH, 'r') as f:
        config = json.load(f)
    return config

# 更新元数据配置文件
def update_config(new_config):
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(new_config, f, indent=4)

# 读取特定domain的配置
def get_domain_config(domain):
    config = read_config()
    domain_config = config['data'].get(domain, {})
    return domain_config

# 更新特定domain和变量的配置
def update_domain_variable_config(domain, variable, updated_config):
    config = read_config()
    if domain in config['data'] and variable in config['data'][domain]:
        config['data'][domain][variable] = updated_config
        update_config(config)
        return {"message": "Config updated successfully"}
    else:
        return {"error": "Domain or variable not found"}

# 读取变量描述文件和数据
def read_output():
    print(f"Trying to read file at: {OUTPUT_FILE_PATH}")
    print(f"Absolute path: {os.path.abspath(OUTPUT_FILE_PATH)}")
    
    if not os.path.exists(OUTPUT_FILE_PATH):
        print(f"File does not exist: {OUTPUT_FILE_PATH}")
        return {}

    with open(OUTPUT_FILE_PATH, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            print("Reading file line by line for debugging:")
            with open(OUTPUT_FILE_PATH, 'r') as debug_f:
                for i, line in enumerate(debug_f):
                    print(f"Line {i + 1}: {line.strip()}")
            raise
    return data

# 更新变量描述文件和数据
def update_output(new_data):
    with open(OUTPUT_FILE_PATH, 'w') as f:
        json.dump(new_data, f, indent=4)

# 处理并返回输出数据（描述信息和数据）
def get_processed_output():
    data = read_output()
    
    # 提取描述信息和数据
    if isinstance(data, list) and len(data) > 0:
        descriptions = data[0]
        records = data[1:]
    else:
        descriptions = {}
        records = []
    
    return {"descriptions": descriptions, "records": records}
