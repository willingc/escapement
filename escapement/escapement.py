"""Main module."""
import json

from escapement.query import Query
from escapement.requests_query import run_query
from escapement.report import generate_report, create_dataframe


def escapement():
    """Run a query"""
    q = Query(orgs=['nteract'], repos=['nteract'], user='willingc')
    q.display_settings()
    query_string = q.compose_query()
    result = run_query(query_string)
    generate_report(result)
    create_dataframe(result)
