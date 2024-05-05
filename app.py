import requests
import os

def check_new_commits(repo_owner, repo_name, last_commit_sha=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    
    params = {"sha": last_commit_sha} if last_commit_sha else {}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        commits = response.json()
        
        if commits:
            print("New commits found:")
            for commit in commits:
                print(f"- {commit['commit']['author']['name']}: {commit['commit']['message']}")
        else:
            print("No new commits found.")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")

repo_owner = "prernassp"
repo_name = "CICD_Project"
os.system("echo started >> log.txt")
last_commit_sha = None
check_new_commits(repo_owner, repo_name, last_commit_sha)