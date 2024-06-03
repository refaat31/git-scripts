import requests
import json

username = 'refaat31'

with open('token.txt','r') as f:
    GITHUB_TOKEN = f.read()

# https://github.com/orgs/community/discussions/24382#:~:text=I%20couldn%60t%20get%20private%20repositories%20while%20i%20was%20using%20the%20wrong%20link.
url = f'https://api.github.com/user/repos' 
params = {
    'visibility':'all',
    'per_page':20
}
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',

}

# r = requests.get(url,headers=headers,params=params)
# # print(r.json())
# r = r.json()
# print()
# exit(0)
repos = []

# https://chatgpt.com/share/bb807039-c9ed-4dbd-a7ac-f9c8059e861d

while url:
    r = requests.get(url,headers=headers,params=params)
    if r.status_code == 401:
        if r.json()['message'] == 'Bad credentials':
            print('Please provide a valid token')
            url = None
    
    repos.extend(r.json())
    if 'next' in r.links:
        url = r.links['next']['url']
    else:
        url = None
        
print(len(repos))
