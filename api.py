import json
import requests
import os


api_token = os.environ['PINGDOM_TOKEN']
api_url   = 'https://api.pingdom.com/api/3.1/checks'

head   = {'Authorization': 'Bearer {0}'.format(api_token)}       

def call_api():

    response = requests.get(api_url, headers=head)

    if   response.status_code != 200:
        print('!!Error!! || StatusCode: {0}'.format(response.status_code))
    
    elif response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        
        for i in range(len(data['checks'])):
            hostname = data['checks'][i]['name']
            idef = str(data['checks'][i]['id'])
            status = data['checks'][i]['status']
            print(f"Domain: {hostname} || ID: {idef} || Status: {status} ")

    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))


call_api()  


