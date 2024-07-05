#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
i
"""
if __name__ == '__main__':
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    i = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = get(URL)
    json = response.json()

    for element in json:
        if i > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
