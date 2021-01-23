"""Main module."""
from . import orgs

ORGS = ['jupyterhub', 'jupyter', 'nteract']
start_date = '2021-01-01'
end_date = '2021-01-21'
# GH_TOKEN get from .env


def escapement():
    orgs.list_orgs(ORGS)
