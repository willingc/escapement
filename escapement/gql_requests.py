from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


def query_gql_requests():
    """Query using gql to GitHub v4"""
    transport = RequestsHTTPTransport(
        url=GH_GQL_ENDPOINT,
        headers={"Authorization": f"token {GH_TOKEN}"},
        verify=True,
        retries=3,
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
