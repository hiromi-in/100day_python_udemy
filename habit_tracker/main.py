import requests, datetime


#----------Create a user account--------------#
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = XXXX
USERNAME = XXXX

pixela_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}



#response = requests.post(url=pixela_endpoint, json=pixela_params)
#print(response.text)

#----------------Create a graph----------------------------#
#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
#graph_config = {
#    "id": "heyheyjayjay",
#    "name": "Study Graph",
#    "unit": "minute",
#    "type": "float",
#    "color" : "ichou",
#}
#
#headers = {
#    "X-USER-TOKEN" : TOKEN
#}
#
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
#


#--------------------put info in the graph---------------------#
GRAPH_ID = "heyheyjayjay"
#
headers = {
    "X-USER-TOKEN" : TOKEN,
}
#
today = datetime.datetime.today().strftime("%Y%m%d")
#
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_update_params = {
    "date" : today,
    "quantity": input("How many minutes did I study today? "),
}

response = requests.post(url=graph_update_endpoint, json=graph_update_params, headers=headers)
print(response.text)
#
#
#-------------Delete an input--------------------#
#delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#
#delete_response = requests.delete(url=delete_endpoint, headers=headers)
#print(delete_response.text)

#--------------Update the input-----------------#
#update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#
#request_body = {
#    "quantity" : "75"
#}
#
#update_response = requests.put(url=update_endpoint, headers=headers, json=request_body)
#print(update_response.text)