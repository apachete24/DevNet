import json
import requests
requests.packages.urllib3.disable_warnings()

# rescatar la configuración de las interfaces
api_url = "https://64.103.37.51:9443/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}
basic_auth = ("developer", "C1sco12345")

resp = requests.get(api_url, auth=basic_auth, headers=headers, verify=False)
resp_jason = resp.json()
print(json.dumps(resp_jason, indent=4))

# modificar la configuración de una interfaz (machaca)
yang_config = {

    "itef-interfaces:interface": {
        "name": "Loopback_lol23",
        "description": "tonto el que lo lea",
        "type": "iana-if-type:softwareLoopback",
        "enable":True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "94.34.80.00",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
