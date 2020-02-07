import json
import requests
import os


api_token = os.environ['PINGDOM_TOKEN']
api_url   = 'https://api.pingdom.com/api/3.1/checks'

headers   = {
            'Content-Type' : 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token) 
            }

print(headers)

def call_api():

    response = requests.get(api_url, headers=headers)

    if response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None  
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None
  

call_api()  

