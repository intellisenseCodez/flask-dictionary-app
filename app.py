from flask import Flask, request, render_template, redirect
import requests
import json


# an instance of Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", result=None)


@app.route("/word", methods=["POST", "GET"])
def getMeaning():
    if request.method == "POST":
        word = request.form["word"]
        print(word)
        if word:
            result = searchWord(word)

            return render_template("index.html", result=result)


def searchWord(word):
    # free dictionaryAPI
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    # make a url request
    response = requests.get(url=url)

    # check response code
    if response.status_code == 200:
        # log
        print("SUCCESSFULLY CONNECTED")

        # get response in json
        data = response.json()

    
        result = {}
        result["word"] = data[0]["word"]
        result["phonetic"] = data[0]["phonetics"][1]["text"]
        result["pos"] = data[0]["meanings"][0]["partOfSpeech"]
        result["definition"] = data[0]["meanings"][0]["definitions"][0]["definition"]

        return result

    else:
        print("INVALID CONNECTION")

if __name__ == "__main__":
    app.run(debug=False)



