# a sample service to read and update json files

import json

# read the specified presetation json file
def read_json():
    with open('tests/outputs/interact/LB.json', 'r') as f:
        data = json.load(f)
    return data


# def read_config():
#     with open('app/config.json', 'r') as f:
#         config = json.load(f)
#     return config

# def update_config(new_config):
#     with open('app/config.json', 'w') as f:
#         json.dump(new_config, f, indent=4)

# def get_processed_output():
#     data = read_json()
#     config = read_config()
    
#     # 假设我们在预览时需要根据配置文件修改某些变量
#     # 这里的逻辑可以根据具体需求进行调整
#     for item in data['items']:
#         if 'configurable_field' in item:
#             item['configurable_field'] = config.get('configurable_field', item['configurable_field'])
    
#     return data
