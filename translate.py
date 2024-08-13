import requests
import json

# API Access values
subscription_key = '9d1f90f2f2b747578dc20d89f11cc5aa'  
endpoint = 'https://api.cognitive.microsofttranslator.com'  
location = 'southeastasia' 

# API path for translation
path = '/translate'

# Request parameters
params = {
    'api-version': '3.0',  # API version
    'from': 'fr',  # Source language
    'to': 'vi'     # Target language
}

# Request headers
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-Type': 'application/json'
}

# Request body
body = [{
    'text': 'Bonjour'  # Text to translate
}]

# Send POST request
response = requests.post(endpoint + path, params=params, headers=headers, json=body)

# Print the response
print(response.json())

