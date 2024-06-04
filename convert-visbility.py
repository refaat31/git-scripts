import requests
import json

def convert_visibility(option:int,owner,repo):
    """
    option = 1 (public to private)
    option = 2 (private to public)
    """
    
    try:
        with open('token.txt','r') as f:
            GITHUB_TOKEN = f.read()
    except:
        print('Error: Please create a token.txt file with valid token.')
        exit(1)
    
    url = f'https://api.github.com/repos/{owner}/{repo}'
    headers = {
        'Content-Type':'application/json',
        'Authorization': f'token {GITHUB_TOKEN}',
    }

    if option == 1:
        data = {
            'private':True
        }
        r = requests.patch(url, headers=headers, data=json.dumps(data))
    elif option == 2:
        data = {
            'private':False
        }
        r = requests.patch(url, headers=headers, data=json.dumps(data))
    
    print(r.text)

convert_visibility(1,'refaat31','repo-name')