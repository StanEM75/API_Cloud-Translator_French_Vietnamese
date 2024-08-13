from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.content_type == 'application/json':
        data = request.json
        text = data.get('text')
    else:
        text = request.form.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    subscription_key = os.getenv('SUBSCRIPTION_KEY')
    endpoint = os.getenv('ENDPOINT')
    location = os.getenv('LOCATION')

    path = '/translate'
    constructed_url = os.path.join(endpoint, path.lstrip('/'))

    params = {
        'api-version': '3.0',
        'to': 'vi'  # Change to 'vi' for Vietnamese
    }
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Region': location
    }
    body = [{'text': text}]

    response = requests.post(constructed_url, params=params, headers=headers, json=body)

    if response.status_code == 200:
        translation = response.json()
        return render_template('index.html', translation=translation[0]['translations'][0]['text'])
    else:
        return jsonify({'error': 'Translation failed'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)


