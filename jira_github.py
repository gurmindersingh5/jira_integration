from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import numpy as np
app = Flask(__name__)
url = "https://gurminderbarca.atlassian.net/rest/api/2/issue"
api_token = 'ATATT3xFfGF0f_u_NCnbPGykflix97zdNdL84tVhmu-1w2gFBfxLi1cahaoUIWSM2QfqaWnqtVX-GZQia8l6izGtb3E4B8UKqhAOsESA-KpTARbOBHYqjsO1BI01I5cqiZVMym6zLQbcejn8nNrILGp-xaoQ-BkVF_pAar47dRE7N4oDlYVIDYg=3DD25483'
auth = HTTPBasicAuth("gurminder.barca@gmail.com", api_token)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        check = data['comment']['body']
        if check == '/jira':
            # Headers for the request
            headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
            }

            # Data for creating the issue
            payload = {
            "fields": {
                "project": {
                "key": "TP"  # Replace with your project key
                },
                "summary": f"Issue {np.random.randint(1,1000)} created via API",
                "description": "Description of the issue created via API",
                "issuetype": {
                "name": "Task"  # Replace with the issue type you want to create
                }
            }
            }
            # Make the POST request to create an issue
            response = requests.post(url, headers=headers, auth=auth, data=json.dumps(payload))

            # Check if the request was successful
            if response.status_code == 201:
                # Parse and print the JSON response
                response_json = response.json()
                return(json.dumps(response_json, sort_keys=True, indent=4, separators=(",", ": ")))
            else:
                # Print the error if the request was not successful
                print(f"Failed to create issue: {response.status_code}")
                return(response.text)
        else:
            return 'NOT POSTED TO JIRA'
    else:
        'METHOD NOT POST'
    return 'NOTHING HAPPENED'




if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True) 
