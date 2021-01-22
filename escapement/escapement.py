"""Main module."""
from . import orgs

ORGS = ['jupyterhub', 'jupyter', 'nteract']


def escapement():
    orgs.list_orgs(ORGS)
