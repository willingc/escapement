# An example to get the remaining rate limit using the Github GraphQL API.

import requests

headers = {"Authorization": "Bearer e2a51bc6c5cdbea017e9ebaa306478360f1de198"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
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

result = run_query(query) # Execute the query
print(result)
