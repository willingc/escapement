from decouple import config

GH_TOKEN = config("GH_TOKEN", default="")
GH_USER = config("GH_USER", default="")
GH_GQL_ENDPOINT = "https://api.github.com/graphql"
GH_REST_ENDPOINT = ""

TARGET_ORGS = ["jupyterhub", "jupyter", "nteract", "jupyter-widgets"]
TARGET_REPOS = []
START_DATE = "2021-01-01"
STOP_DATE = "2021-01-21"
