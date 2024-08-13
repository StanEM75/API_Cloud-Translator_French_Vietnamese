from flask import Flask, request, render_template, jsonify
from urllib.parse import quote as url_quote
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Check content type and retrieve text accordingly
    if request.content_type == 'application/json':
        data = request.json
        text = data.get('text')
    else:
        text = request.form.get('text')

    # Validate the input
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Retrieve environment variables for Azure Translator API
    subscription_key = os.getenv('SUBSCRIPTION_KEY')
    endpoint = os.getenv('ENDPOINT')
    location = os.getenv('LOCATION')

    if not all([subscription_key, endpoint, location]):
        return jsonify({'error': 'Translation service configuration is missing'}), 500

    # Construct the API endpoint URL
    path = '/translate'
    constructed_url = os.path.join(endpoint, path.lstrip('/'))

    # Define the API request parameters
    params = {
        'api-version': '3.0',
        'to': 'vi'  # Target language code, change as needed
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Region': location
    }
    body = [{'text': text}]

    # Make the API request
    response = requests.post(constructed_url, params=params, headers=headers, json=body)

    # Handle the API response
    if response.status_code == 200:
        translation = response.json()
        translated_text = translation[0]['translations'][0]['text']
        return render_template('index.html', translation=translated_text)
    else:
        return jsonify({'error': 'Translation failed', 'details': response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

