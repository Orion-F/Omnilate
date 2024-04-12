from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translations = {}
    if request.method == 'POST':
        word = request.form.get('word')
        if word:
            languages = ['en', 'de', 'fr', 'pl', 'uk']
            language_names = {'en': 'English', 'de': 'German', 'fr': 'French', 'pl': 'Polish', 'uk': 'Ukrainian'}
            translations = {language_names[lang]: GoogleTranslator(source='en', target=lang).translate(word)
                            for lang in languages}
    return render_template('index.html', translations=translations)

if __name__ == '__main__':
    app.run(debug=True)
