import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://64.103.37.51:9443/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}
basic_auth = ("developer", "C1sco12345")
resp = requests.get(api_url, auth=basic_auth, headers=headers, verify=False)
