from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

GH_GQL_ENDPOINT = "https://api.github.com/graphql/"

GH_USER='willingc'
GH_TOKEN = 'e2a51bc6c5cdbea017e9ebaa306478360f1de198'

transport = RequestsHTTPTransport(
    url=GH_GQL_ENDPOINT, headers={'Authorization': 'token e2a51bc6c5cdbea017e9ebaa306478360f1de198'},verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    {
    organization(login: "jupyterhub") {
        repositories(first: 100) {
        totalCount
        edges {
            node {
            name
            url
            issues(states: OPEN) {
                totalCount
            }
            pullRequests(states: OPEN) {
                totalCount
            }
            }
        }
        }
    }
    }
"""
)

# Execute the query on the transport
result = client.execute(query)
print(result)
