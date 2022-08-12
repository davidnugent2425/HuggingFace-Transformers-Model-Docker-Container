from flask import Flask, request, jsonify
# from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
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

    # model_path = './models/transformers/' 
    # model = TFAutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
    # print("----------- transformer model loaded ------------")
    # tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    # print("----------- transformer tokenizer loaded ------------")
    # classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    # print(classifier)
    classifier = pipeline("fill-mask", model="camembert-base")

    app.run(debug=True, host='0.0.0.0')

