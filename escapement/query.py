"""Query GitHub API v4 GraphQL or v3 REST"""
import requests



GH_GQL_ENDPOINT = "https://api.github.com/graphql"



def connect(url):
    """Connect to GitHub endpoint"""
    return

def display_query_options():
    return

def prepare_query():
    # Query content to use in request

def connect_enterprise_account(url, token):
    # Query a private enterprise account org

    query="""curl \
    -i -u willingc:$GITHUB_ACCESS_TOKEN \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/orgs/noteable-io/repos\?type\=private
    """
    # GITHUB_ACCESS_TOKEN should have read access for repo and enterprise access
