from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
payload = {}

rasa_endpoint = 'http://localhost:5005/webhooks/rest/webhook'
ip = '192.168.44.1'


@app.route('/webhooks/rest/webhook', methods=['POST'])
def process_request():
    data = request.get_json()
    print(data)
    print("data: "+str(data))
    payload['recipient_id'] = data['sender']
    payload['message'] = data['message']
    payload_json = json.dumps(payload)
    sendBack = requests.post(rasa_endpoint, data=payload_json, )
    response_data = sendBack.json()
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host=ip, port=4000, debug=True)
