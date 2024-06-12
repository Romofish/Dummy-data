# Pending May not using this file

from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Dataset(BaseModel):
    id: int
    name: str
    data: dict

datasets = []

@app.get("/datasets")
def get_datasets():
    return datasets

@app.get("/datasets/{dataset_id}")
def get_dataset(dataset_id: int):
    for dataset in datasets:
        if dataset['id'] == dataset_id:
            return dataset
    return {"error": "Dataset not found"}

@app.post("/datasets")
def create_dataset(dataset: Dataset):
    datasets.append(dataset.dict())
    return dataset

@app.put("/datasets/{dataset_id}")
def update_dataset(dataset_id: int, updated_dataset: Dataset):
    for i, dataset in enumerate(datasets):
        if dataset['id'] == dataset_id:
            datasets[i] = updated_dataset.dict()
            return updated_dataset
    return {"error": "Dataset not found"}

@app.delete("/datasets/{dataset_id}")
def delete_dataset(dataset_id: int):
    global datasets
    datasets = [dataset for dataset in datasets if dataset['id'] != dataset_id]
    return {"message": "Dataset deleted"}
