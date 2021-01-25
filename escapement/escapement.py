"""Main module."""
from escapement.builder import Query
from escapement.requests_query import run_query
from escapement.report import generate_report


def escapement():
    """Run a query"""
    q = Query(orgs=['jupyter'], repos=['notebook', 'nbconvert'], user='willingc')
    q.display_settings()
    q.compose_query()
    #result = run_query()
    #generate_report(result)
