# An example to get the remaining rate limit using the Github GraphQL API.

import requests

from escapement.defaults import GH_TOKEN, GH_GQL_ENDPOINT


headers = {"Authorization": f"Bearer {GH_TOKEN}"}
# The GraphQL query (with a few additional bits included) itself defined as a multi-line string.
new_query = """
{
repository(owner: "jupyter", name: "jupyter_client") {
    pullRequest(number: 261) {
    comments(first: 40) {
        nodes {
        body
        }
        }
    }
    }
}
"""

def run_query():
    """Run query using requests to graphql endpoint"""
    request = requests.post(GH_GQL_ENDPOINT,
        json={'query': new_query}, headers=headers)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, new_query))

