from flask import Flask, request, jsonify
from transformers import pipeline

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
    classifier = pipeline("fill-mask", model="camembert-base")
    app.run(debug=True, host='0.0.0.0')

