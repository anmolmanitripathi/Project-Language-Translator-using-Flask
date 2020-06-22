from flask import Flask, request, url_for, redirect, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            text_to_translate = request.form["text-to-translate"].lower()
            selected_language = request.form["select-language"]
            translated_text = translator.translate(
                text_to_translate, dest=selected_language)
            text = translated_text.text
            pronunciation_data = translated_text.pronunciation
            if (str(pronunciation_data) == "None"):
                pronunciation_data = "{Sorry, data not available}"
            confidence = round((translator.translate(
                text_to_translate, dest=selected_language).extra_data["confidence"])*100, 2)
        except:
            pronunciation_data = "-"
            text = "{ERROR: We are not able to handle your request right now}"
            confidence = "-"
        return render_template('index.html', translation_result=text, pronunciation=pronunciation_data, confidence_level=str(confidence)+" %")
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
