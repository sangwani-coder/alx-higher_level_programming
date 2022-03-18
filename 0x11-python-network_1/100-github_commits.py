#!/usr/bin/python3
""" Lists 10 commits from the most recent to oldest of the
    repository "rails" by the user "rails"
    Usage:
            ./100-github_commits.py <repo name> <owner>
"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                  commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
