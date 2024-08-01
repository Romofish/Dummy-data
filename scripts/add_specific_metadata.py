import pandas as pd
import json

# 读取Excel文件中的两个Sheet
excel_path = 'metadata/definitions/Stage Metadata from MDRLite.xlsx'
df_vars = pd.read_excel(excel_path, sheet_name='Suffix Decode')
df_ct = pd.read_excel(excel_path, sheet_name='CT', keep_default_na=False)  # 读取时不将NA转换为NaN

# 读取JSON文件
json_path = 'metadata/default_metadata.json'
with open(json_path, 'r') as file:
    metadata = json.load(file)

# 构建CT字典
ct_dict = {}
for name in df_ct['Name'].unique():
    entries = df_ct[df_ct['Name'] == name]['Entries'].tolist()
    ct_dict[name] = entries

# 遍历JSON数据并进行匹配和更新
for domain, variables in metadata.get('data', {}).items():
    for var_name, details in variables.items():
        if not details["Controlled Terms, Codelist or Format"][0]:  # 如果CT字段为空
            # 从Suffix Decode表中查找对应的CT信息
            ct_name = df_vars[df_vars['Vars'] == var_name]['CT_Name'].values
            if len(ct_name) > 0 and pd.notna(ct_name[0]):  # 确保CT_Name不为空
                ct_name = ct_name[0]
                if ct_name in ct_dict:
                    details["Controlled Terms, Codelist or Format"] = ct_dict[ct_name]
                else:
                    print(f"No CT found for variable: {var_name} with CT_Name: {ct_name}")
            else:
                print(f"No CT_Name found for variable: {var_name}, retaining original JSON data")

# 保存更新后的JSON数据
output_path = 'metadata/default_metadata_MDRLITE.json'
with open(output_path, 'w') as file:
    json.dump(metadata, file, indent=4)
print(f"Updated metadata saved to {output_path}")
