
from ghapi.all import GhApi
from datetime import datetime
import os

github_token = os.getenv('GITHUB_TOKEN')

repo_list = [
    ("https://github.com", "NatLabRockies", "floris"),
    ("https://github.com", "openfast", "openfast"),
    ("https://github.com", "exawind", "nalu-wind"),
    ("https://github.com", "exawind", "amr-wind"),
    ("https://github.com", "NatLabRockies", "windse"),
    ("https://github.com", "erf-model", "erf"),
    ("https://github.com", "openfast", "kitefast"),
    ("https://github.com", "openfast", "openfast"),
    ("https://github.com", "sandialabs", "OWENS.jl"),
    ("https://github.com", "NatLabRockies", "rosco"),
    ("https://github.com", "NatLabRockies", "rosco_toolbox"),
    ("https://github.com", "wisdem", "wisdem"),
    ("https://github.com", "wisdem", "weis"),
    ("https://github.com", "NatLabRockies", "HOPP"),
    ("https://github.com", "NLRWindSystems", "landbosse"),
    ("https://github.com", "NLRWindSystems", "WOMBAT"),
    ("https://github.com", "NLRWindSystems", "ard"),
]

for repo in repo_list:
    api = GhApi(owner=repo[1], repo=repo[2], token=github_token)
    # api = GhApi(owner="NatLabRockies", repo="floris")

    # Determine the primary branch
    primary_branch = None
    branches = api.list_branches()
    for b in branches:
        name = b["ref"].replace("refs/heads/", "")
        if name == "main":
            primary_branch = "main"
        elif name == "master":
            primary_branch = "master"

    if primary_branch is None:
        print(f"Primary branch not found for {repo[1]}/{repo[2]}")
        continue

    # Get the last commit from primary branch
    main = api.get_branch(primary_branch)
    main_commit = api.git.get_commit(main["object"]["sha"])
    last_commit_date = datetime.fromisoformat(main_commit["committer"]["date"]).strftime("%b %d %Y")

    releases = api.repos.list_releases()
    if len(releases) < 1:
        last_release_date = ""
    else:
        last_release_date = datetime.fromisoformat(releases[0]["published_at"]).strftime("%b %d %Y")

    print(f"{last_commit_date}, {last_release_date}")
