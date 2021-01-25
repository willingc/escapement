"""Queries using Requests"""
import requests

from escapement.defaults import GH_TOKEN, GH_GQL_ENDPOINT


headers = {"Authorization": f"Bearer {GH_TOKEN}"}

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
    print("Sending a query to GH GQL using requests")
    request = requests.post(GH_GQL_ENDPOINT, json={"query": new_query}, headers=headers)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            f"Query failed to run by returning code of {request.status_code}. {new_query}"
        )
