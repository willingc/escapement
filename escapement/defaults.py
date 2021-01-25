from decouple import config

# credentials
GH_TOKEN = config("GH_TOKEN", default="")
GH_USER = config("GH_USER", default="")

# endpoints
GH_GQL_ENDPOINT = "https://api.github.com/graphql"
GH_REST_ENDPOINT = ""

# targets
TARGET_ORGS = ["jupyterhub", "jupyter", "nteract", "jupyter-widgets"]
TARGET_REPOS = []

# date and time
START_DATE = "2021-01-01"
STOP_DATE = "2021-01-21"


def display_credentials():
    """Display the GitHub credentials"""
    print(f"GH_TOKEN: {GH_TOKEN}")
    print(f"USER: {GH_USER}")
