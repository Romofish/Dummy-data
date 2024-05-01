import os
from dotenv import load_dotenv
import json

# 加载环境变量
load_dotenv()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON - {file_path}")
        return {}

def merge_files(data_file, control_file, output_file):
    metadata = load_json(data_file)
    control_terms = load_json(control_file)

    # 构建术语字典
    terminology_dict = {}
    for term_description, details in control_terms.get('data', {}).items():
        for term_name, values in details.items():
            terminology_dict[term_name] = values

    # 合并数据
    for domain, variables in metadata.get('data', {}).items():
        for var, details in variables.items():
            controlled_term = details.get("Controlled Terms, Codelist or Format", "").strip()
            if controlled_term in terminology_dict:
                details["Controlled Terms, Codelist or Format"] = terminology_dict[controlled_term]
            else:
                details["Controlled Terms, Codelist or Format"] = [controlled_term]

    # 写入合并后的数据到新文件
    with open(output_file, 'w') as file:
        json.dump(metadata, file, indent=4)
    print(f"Data merged and saved to {output_file}")

# 输入文件路径和输出文件路径
metadata_path = os.getenv("VARIABLES_PATH")
codelists_path = os.getenv("CODELISTS_PATH")
output_file = 'metadata/merged_vars.json'

# 执行合并操作
merge_files(metadata_path, codelists_path, output_file)

