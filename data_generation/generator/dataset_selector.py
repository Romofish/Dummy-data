# dataset_selector.py
import json

def select_datasets(metadata, selection=None):
    """ Return only selected datasets or all if no selection is made """
    if not selection:
        return metadata['data']
    else:
        return {k: v for k, v in metadata['data'].items() if k in selection}
