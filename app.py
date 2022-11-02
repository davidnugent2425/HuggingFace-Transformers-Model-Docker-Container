from flask import Flask, request, jsonify
from transformers import pipeline
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def makecalc():
    if request.method=="POST":
        data = request.get_json()
        print("data ---- > ", data)
        results = classifier(data)
        
        return jsonify(results)
    return "Not a proper request method or data"


if __name__ == '__main__':
    print('waiting 30 seconds before trying to download model...')
    time.sleep(30)
    classifier = pipeline("fill-mask", model="bert-base-uncased")
    app.run(debug=True, host='0.0.0.0')

