from transformers import pipeline

from flask import Flask, request

app = Flask(__name__)

GENERATOR = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')


@app.route("/")
def home():
    return "Test"


@app.route("/text_generation/", methods=["POST", "OPTIONS"])
def text_generation():
    files = request.files

    text = files["text"]

    prediction = GENERATOR(text)

    return {
        "textOutput": prediction,
        "textInput": text
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
