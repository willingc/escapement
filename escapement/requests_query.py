"""Queries using Requests"""
import json

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


def run_query(query_string):
    """Run query using requests to graphql endpoint"""
    if query_string is not None:
        print("Sending a query to GH GQL using requests")
        response = requests.post(GH_GQL_ENDPOINT,
            json={"query": query_string},
            headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Query failed with return code {response.status_code}."
            )
    else:
        raise Exception(
            f"No query string was passed."
        )
