#!/usr/bin/python3
""" Python script that lists 10 most recent commits from a given
    repository. Arguments passed are owner_name and repository_name
    """
import requests
import sys


def fetch_commits(owner, repo, number=10):
    """ Using the github API, format the url and prob it to return the
    response to the requests call. Retrieving 10 commits.
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': number}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def display_commits(commits):
    """ This function difinition diplays the commits """
    if commits:
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits.")


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = fetch_commits(owner_name, repository_name)
    display_commits(commits)
