import requests
import json
from tabulate import *

def get_ticket ():


#datos de conexion
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"

    headers = {
         "content-type": "application/json"
    }

    body_json = {
         "username": "devnetuser",
         "password": "Cisco123!"
    }

# petición
    reply = requests.post(api_url, json.dumps(body_json), headers=headers, verify=None)
    print("Request Status: ", reply.status_code)
    response_json = reply.json()
    ticket = response_json["response"]["serviceTicket"]
    return ticket




#Imprime la información seleccionada de las interfaces del host en forma de tabla
def print_hosts ():

    #datos para establecer la conexión
    ticket = get_ticket()
    api_url = "https://sandboxapicem.cisco.com/api/v1/host"
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }

    # petición
    resp = requests.get(api_url, headers=headers, verify=None)
    #comprobacion
    print("Status Code: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception("Status code not equal 200. Response text: ", resp.text)
    #convertir la respuesta a json
    response_json = resp.json()

    host_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        host = [
            i,
            item["hostType"],
            item["hostIp"],
            item["hostMac"]
        ]
        host_list.append(host)

    table_header = ["Number", "Type", "IP", "MAC"]
    print(tabulate(host_list, table_header))







def print_devices():
    # NETWORK-DEVICE API URL
    #api_url = "https://{YOUR-APICEM}.cisco.com/api/v1/network-device"
    api_url = "https://sandboxapicem.cisco.com/api/v1/network-device"

    # Setup API request headers.
    ticket = get_ticket()
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of GET /network-device request: ", resp.status_code)  # This is the http request status
    # Check if the request status was 200/OK
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    # Get the json-encoded content from response
    response_json = resp.json()  

    # Now create a list of host summary info
    device_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        device = [
                    i, 
                    item["type"], 
                    item["managementIpAddress"] 
                 ]
        device_list.append( device )

    table_header = [
                    "Number", 
                    "Type", 
                    "IP"
                   ]
    print( tabulate(device_list, table_header) )
 
