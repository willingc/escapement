"""
Script to get watchers/stars/forks for all repos on a github organization

Set GITHUB_API_TOKEN environment variable if you are hitting the API rate limit

Requires pygithub and Python 3.6:

    pip install pygithub

Usage:

    python org-activity.py <org-name>

e.g.

    python org-activity.py binder-examples

LICENSE: CC-0 or Public Domain
"""

import os
import sys

# pip install pygithub
from github import Github as GitHub  # fix case!


def main(org_name):
    gh = GitHub()
    if "GITHUB_API_TOKEN" in os.environ:
        gh = GitHub(os.environ["GITHUB_API_TOKEN"])
    else:
        gh = GitHub()
    org = gh.get_organization(org_name)

    totals = {
        "watchers": 0,
        "stars": 0,
        "forks": 0,
    }
    print(f"{'repo':40} {'watch'} {'stars'} {'forks'}")
    for repo in org.get_repos():

        print(
            f"{repo.full_name:40}"
            f" {repo.watchers_count:5}"
            f" {repo.stargazers_count:5}"
            f" {repo.forks_count:5}"
        )
        totals["watchers"] += repo.watchers_count
        totals["stars"] += repo.stargazers_count
        totals["forks"] += repo.forks_count

    print("\nTotals:")
    for key, value in totals.items():
        print(f"{key:8}: {value:4}")


if __name__ == "__main__":
    main(sys.argv[1])
