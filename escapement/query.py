"""Query builder"""
from escapement.defaults import GH_TOKEN, GH_GQL_ENDPOINT


composed_query = """
{
  repository(name: "nteract", owner: "nteract") {
    name
    issues(last: 10) {
      edges {
        node {
          number
          title
          url
        }
      }
    }
  }
}
"""


class Query:
    """A graphql query"""
    def __init__(self, orgs=None, repos=None, user=None, query_template=None):
        self.orgs = orgs
        self.repos = repos
        self.user = user
        self.query_template = query_template
        self.configured_query = composed_query


    def display_settings(self):
        print('Displaying query settings...')
        print(f'Orgs: {self.orgs}')
        print(f'Repos: {self.repos}')
        print(f'User: {self.user}')
        print(f'Query template: {self.query_template}')


    def compose_query(self):
        """Compose a gql query"""
        print(f'{self.orgs} {self.repos}')
        configured_query = self.configured_query
        return configured_query
