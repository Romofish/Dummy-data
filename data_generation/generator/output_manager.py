# output_manager.py
import json
import pandas as pd

def save_to_file(df, dataset_name, path, formats):
    """Save dataset to specified formats in the specified path."""
    if 'json' in formats:
        full_path_json = f"{path}/{dataset_name}.json"
        df.to_json(full_path_json, orient='records', lines=True, force_ascii=False, indent=4)
        print(f"Data for {dataset_name} saved to {full_path_json}")

    if 'excel' in formats:
        full_path_excel = f"{path}/{dataset_name}.xlsx"
        df.to_excel(full_path_excel, index=False)
        print(f"Data for {dataset_name} saved to {full_path_excel}")

    if 'csv' in formats:
        full_path_csv = f"{path}/{dataset_name}.csv"
        df.to_csv(full_path_csv, index=False)
        print(f"Data for {dataset_name} saved to {full_path_csv}")


