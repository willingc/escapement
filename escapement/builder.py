"""Query builder"""
from escapement.defaults import GH_TOKEN, GH_GQL_ENDPOINT


class Query:
    """A graphql query"""
    def __init__(self, orgs=None, repos=None, user=None, query_template=None):
        self.orgs = orgs
        self.repos = repos
        self.user = user
        self.query_template = query_template


    def display_settings(self):
        print(f'Orgs: {self.orgs}')
        print(f'Repos: {self.repos}')
        print(f'User: {self.user}')
        print(f'Query template: {self.query_template}')


    def build_query(orgs=None, repos=None, user=None, query_template=None):
        """Build a gql query"""

