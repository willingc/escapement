from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

GH_GQL_ENDPOINT = "https://api.github.com/graphql"


# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=GH_GQL_ENDPOINT)

# Create a GraphQL client using the defined transport
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
