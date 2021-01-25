"""Report"""
import json


def generate_report(results):
    """Display as a report"""
    print(json.dumps(results, indent=2, sort_keys=True))
