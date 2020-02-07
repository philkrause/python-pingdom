import json
import requests
import os


api_token = os.environ['PINGDOM_TOKEN']
api_url   = "https://api.pingdom.com/api/3.1/checks"

auth = 'Bearer ' + api_token

head   = {
            "Content-Type" : "application/json",
            "Authorization": auth
            }       

def call_api():

    response = requests.get(api_url, headers=head)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))

        print(data)
        return data
    else:
        print("You suck at coding. Have Jen fix this.")

call_api()  

