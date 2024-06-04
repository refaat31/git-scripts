import requests
import json
import csv
# import pandas as pd

username = 'refaat31'

try:
    with open('token.txt','r') as f:
        GITHUB_TOKEN = f.read()
except:
    print('Error: Please create a token.txt file with valid token.')
    exit(1)

# https://github.com/orgs/community/discussions/24382#:~:text=I%20couldn%60t%20get%20private%20repositories%20while%20i%20was%20using%20the%20wrong%20link.
url = f'https://api.github.com/user/repos' 
params = {
    'visibility':'all',
    'per_page':20
}
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',

}

repos = []

# https://chatgpt.com/share/bb807039-c9ed-4dbd-a7ac-f9c8059e861d
while url:
    r = requests.get(url,headers=headers,params=params)
    if r.status_code == 401:
        if r.json()['message'] == 'Bad credentials':
            print('Error: Please provide a valid token')
            exit(1)
    
    repos.extend(r.json())
    if 'next' in r.links:
        url = r.links['next']['url']
    else:
        url = None

# figure out what info we will store in csv
# dict_keys(['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'has_discussions', 'forks_count', 'mirror_url', 'archived', 'disabled', 'open_issues_count', 'license', 'allow_forking', 'is_template', 'web_commit_signoff_required', 'topics', 'visibility', 'forks', 'open_issues', 'watchers', 'default_branch', 'permissions'])


repo_trimmed = []
for r in repos:
    repo_trimmed.append({
        'id': r['id'],
        'full_name': r['full_name'],
        'url': r['url'],
        'private': r['private'],
        'owner': r['owner'],
        'description': r['description'],
        'fork': r['fork'],
        'created_at': r['created_at'],
        'updated_at': r['updated_at']
    })



# https://www.geeksforgeeks.org/writing-csv-files-in-python/
fields = ['id', 'full_name', 'url', 'private', 'owner', 'description', 'fork', 'created_at', 'updated_at']
filename = 'all_repos.csv'

with open(filename, 'w',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(repo_trimmed)