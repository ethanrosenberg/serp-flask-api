from flask import Flask, url_for, jsonify, request
import argparse
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

application = Flask(__name__)

@application.route("/")
def home():
    return "Welcome!"

@application.route("/analyze", methods = ['POST'])
def hello():
    if request.headers['Content-Type'] != 'application/json':
        return "Requests must be in JSON format. Please make sure the header is 'application/json' and the JSON is valid."
    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)

    if client_data["type"] == "SimpleRatio":
        return {"type": client_data["type"], "response": str(fuzz.ratio(client_data['keyword'], client_data['text'])) }
    elif client_data["type"] == "PartialRatio":
        return {"type": client_data["type"], "response": str(fuzz.partial_ratio(client_data['keyword'], client_data['text'])) }
    elif client_data["type"] == "TokenSortRatio":
        return {"type": client_data["type"], "response": str(fuzz.token_sort_ratio(client_data['keyword'], client_data['text'])) }
    elif client_data["type"] == "TokenSetRatio":
        return {"type": client_data["type"], "response": str(fuzz.token_set_ratio(client_data['keyword'], client_data['text'])) }
    else:
        #return str(fuzz.token_set_ratio(client_data['keyword'], client_data['text']))
        return {"type": client_data["type"], "response": str(fuzz.token_set_ratio(client_data['keyword'], client_data['text'])) }
    #fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
    #return str(fuzz.token_set_ratio(client_data['keyword'], client_data['text']))

if __name__ == "__main__":
    application.debug = True
    application.run()
