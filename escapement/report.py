"""Report"""
import json


import pandas as pd


def generate_report(file):
    """Display as a report"""
    print(json.dumps(file, indent=2, sort_keys=True))


def create_dataframe(result):
    """Create a pandas dataframe from a file"""
    print(type(result))
    print(result)
    result_json = json.dumps(result)
    with open('results.json', 'w') as json_file:
        json.dump(result, json_file)


