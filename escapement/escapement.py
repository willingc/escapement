"""Main module."""

from escapement.defaults import GH_TOKEN, GH_USER

# from gql_requests import query_gql_requests
from escapement.requests_query import run_query


def escapement():
    # query_gql()
    # query_rest()
    # query_gql_requests()
    result = run_query()
    print(result)


def display_credentials():
    print(f"GH_TOKEN: {GH_TOKEN}")
    print(f"USER: {GH_USER}")


def query_gql():
    print("Do a gql query")


def query_rest():
    print("Do a REST query")
